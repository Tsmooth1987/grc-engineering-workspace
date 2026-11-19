import boto3
import pandas as pd
import logging
import json

# --- Step 1: Setup Logging & AWS Clients ---
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('iam_policy_alerter.log'), 
        logging.StreamHandler()
    ]
)

logging.info("IAM Policy Alerter script started.")

# --- Step 2: Connect to AWS and Define Resources ---
# Create Boto3 clients for IAM and SNS
iam_client = boto3.client('iam')
sns_client = boto3.client('sns')
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:291846646255:GRC-Alerts" 

# --- Step 2: Connect to AWS and Get IAM Policies ---
policies = []
try:
    logging.info("Connecting to AWS to get IAM policies...")
    # We use Scope='Local' to get only customer-managed policies, not AWS-managed ones.
    response = iam_client.list_policies(Scope='Local')
    policies = response['Policies']
    logging.info(f"Successfully found {len(policies)} customer-managed policies to audit.")
except Exception as e:
    logging.error(f"Could not connect to AWS or fetch IAM policies. Error: {e}")

# This list will hold the details of any admin policies we find.
audit_findings = []


# --- Step 3: Analyze Each Policy Document ---
if policies:
    logging.info("Starting analysis of each policy document...")
    for policy in policies:
        policy_name = policy['PolicyName']
        policy_arn = policy['Arn']
        default_version_id = policy['DefaultVersionId']
        logging.info(f"  - Analyzing policy: {policy_name} ({policy_arn})")

        try:
            # Get the actual policy document from AWS
            version_response = iam_client.get_policy_version(
                PolicyArn=policy_arn,
                VersionId=default_version_id
            )
            policy_document = version_response['PolicyVersion']['Document']

            # The 'Statement' can be a single dictionary or a list of them. Standardize to a list.
            statements = policy_document.get('Statement', [])
            if not isinstance(statements, list):
                statements = [statements]

            # Check each statement in the policy document
            for statement in statements:
                # This is the specific, high-risk pattern we are looking for
                is_admin_access = (
                    statement.get('Effect') == 'Allow' and
                    statement.get('Action') == '*' and
                    statement.get('Resource') == '*'
                )

                if is_admin_access:
                    finding_details = f"Policy '{policy_name}' ({policy_arn}) grants full Administrator Access."
                    logging.warning(f"    - FOUND ADMIN POLICY: {finding_details}")
                    
                    # Add to findings for the report
                    finding = {
                        'PolicyName': policy_name,
                        'PolicyARN': policy_arn,
                        'Finding': "Policy grants full Administrator Access ('Allow', '*', '*')"
                    }
                    audit_findings.append(finding)

                    # --- Step 3b: Send SNS Alert ---
                    try:
                        logging.info(f"      - Sending alert to SNS topic: {SNS_TOPIC_ARN}")
                        subject = f"GRC Alert: Administrator Access Policy Detected!"
                        message = (
                            "An IAM policy with full administrator privileges has been detected in your AWS account.\n\n"
                            f"Policy Name: {policy_name}\n"
                            f"Policy ARN: {policy_arn}\n\n"
                            "This policy should be reviewed immediately to ensure it is intended and necessary."
                        )
                        
                        sns_client.publish(
                            TopicArn=SNS_TOPIC_ARN,
                            Subject=subject,
                            Message=message
                        )
                        logging.info("      - Successfully sent alert.")
                    except Exception as sns_error:
                        logging.error(f"      - FAILED to send SNS alert. Error: {sns_error}")
                    # Once found, we can stop checking other statements in this policy
                    break

        except Exception as e:
            logging.error(f"Could not analyze policy {policy_name}. Error: {e}")

    logging.info("Finished analyzing all policies.")


# --- Step 4: Create and Save the Report ---
if audit_findings:
    logging.info(f"Found {len(audit_findings)} policy/policies with administrator access. Creating CSV report...")
    try:
        df = pd.DataFrame(audit_findings)
        report_path = 'iam_admin_policies_report.csv'
        df.to_csv(report_path, index=False)
        logging.info(f"Successfully saved IAM policy audit report to {report_path}")
    except Exception as e:
        logging.error(f"Could not save the report. Error: {e}")
else:
    logging.info("No policies with administrator access found. No report generated.")


logging.info("IAM Policy Auditor script finished.")
