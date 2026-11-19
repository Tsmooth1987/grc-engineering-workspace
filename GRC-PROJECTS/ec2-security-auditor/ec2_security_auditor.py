import boto3
import pandas as pd
import logging

# --- Step 1: Setup Logging ---
# Configure logging to write to both a file and the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ec2_security_audit.log'),
        logging.StreamHandler()
    ]
)

logging.info("EC2 Security Group Auditor script started.")

# --- Step 2: Connect to AWS and Get Security Groups ---
security_groups = []
try:
    ec2_client = boto3.client('ec2')
    logging.info("Connecting to AWS to get EC2 Security Groups...")
    # describe_security_groups() can handle pagination automatically if needed
    response = ec2_client.describe_security_groups()
    security_groups = response['SecurityGroups']
    logging.info(f"Successfully found {len(security_groups)} security group(s) to audit.")
except Exception as e:
    logging.error(f"Could not connect to AWS or fetch security groups. Error: {e}")

# This list will hold the details of any risky rules we find.
audit_findings = []


# --- Step 3: Analyze Security Group Rules ---
# Define what we consider a sensitive port for this audit.
SENSITIVE_PORTS = [22, 3389] # SSH and RDP

if security_groups:
    logging.info("Starting analysis of security group rules...")
    for group in security_groups:
        group_id = group['GroupId']
        group_name = group['GroupName']
        logging.info(f"  - Analyzing group: {group_name} ({group_id})")

        # Iterate over the inbound rules for the group
        for rule in group.get('IpPermissions', []):
            # Check for rules that allow access from anywhere on the internet
            for ip_range in rule.get('IpRanges', []):
                if ip_range.get('CidrIp') == '0.0.0.0/0':
                    # This rule is open to the world. Now, check the port.
                    from_port = rule.get('FromPort')
                    to_port = rule.get('ToPort')
                    ip_protocol = rule.get('IpProtocol')

                    # Case 1: All traffic is allowed (-1 means all protocols/ports)
                    if ip_protocol == '-1':
                        description = "Allows ALL traffic from Anywhere (0.0.0.0/0)"
                        audit_findings.append({
                            'GroupID': group_id,
                            'GroupName': group_name,
                            'RiskyRule': description
                        })
                        logging.warning(f"    - FOUND RISKY RULE in {group_name}: {description}")
                        continue # Move to the next rule

                    # Case 2: Check for specific sensitive ports
                    for port in SENSITIVE_PORTS:
                        if from_port is not None and to_port is not None and from_port <= port <= to_port:
                            description = f"Allows access to sensitive port {port} ({ip_protocol.upper()}) from Anywhere (0.0.0.0/0)"
                            audit_findings.append({
                                'GroupID': group_id,
                                'GroupName': group_name,
                                'RiskyRule': description
                            })
                            logging.warning(f"    - FOUND RISKY RULE in {group_name}: {description}")
                            # Break to avoid duplicate findings for the same rule if multiple sensitive ports are in range
                            break
    logging.info("Finished analyzing all security groups.")


# --- Step 4: Create and Save the Report ---
if audit_findings:
    logging.info(f"Found {len(audit_findings)} risky rule(s). Creating CSV report...")
    try:
        df = pd.DataFrame(audit_findings)
        report_path = 'security_group_report.csv'
        df.to_csv(report_path, index=False)
        logging.info(f"Successfully saved security group audit report to {report_path}")
    except Exception as e:
        logging.error(f"Could not save the report. Error: {e}")
else:
    logging.info("No risky security group rules found. No report generated.")


logging.info("EC2 Security Group Auditor script finished.")
