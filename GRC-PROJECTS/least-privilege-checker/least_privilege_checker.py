"""
AWS Least-Privilege Compliance Checker
Analyzes IAM policies for least-privilege violations and overly broad permissions.
Author: Terence Webster
"""

import boto3
import pandas as pd
import logging
import json
from datetime import datetime

# --- Setup Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('least_privilege_checker.log'),
        logging.StreamHandler()
    ]
)

logging.info("AWS Least-Privilege Compliance Checker started.")

# --- AWS Clients ---
iam_client = boto3.client('iam')

# --- Violation Patterns ---
VIOLATION_PATTERNS = {
    'full_admin': {
        'name': 'Full Administrator Access',
        'severity': 'CRITICAL',
        'description': 'Policy grants full access to all AWS services and resources'
    },
    'wildcard_actions': {
        'name': 'Wildcard Actions',
        'severity': 'HIGH',
        'description': 'Policy uses wildcard (*) for actions'
    },
    'wildcard_resources': {
        'name': 'Wildcard Resources',
        'severity': 'HIGH',
        'description': 'Policy uses wildcard (*) for resources'
    },
    'overly_broad_service': {
        'name': 'Overly Broad Service Access',
        'severity': 'MEDIUM',
        'description': 'Policy grants full access to specific service (e.g., s3:*)'
    },
    'notaction_usage': {
        'name': 'NotAction Usage',
        'severity': 'MEDIUM',
        'description': 'Policy uses NotAction which can be overly permissive'
    }
}

def get_customer_managed_policies():
    """Fetch all customer-managed IAM policies"""
    policies = []
    try:
        logging.info("Fetching customer-managed IAM policies...")
        paginator = iam_client.get_paginator('list_policies')
        for page in paginator.paginate(Scope='Local'):
            policies.extend(page['Policies'])
        logging.info(f"Found {len(policies)} customer-managed policies")
    except Exception as e:
        logging.error(f"Error fetching policies: {e}")
    return policies

def get_policy_document(policy_arn, version_id):
    """Retrieve the policy document for a specific version"""
    try:
        response = iam_client.get_policy_version(
            PolicyArn=policy_arn,
            VersionId=version_id
        )
        return response['PolicyVersion']['Document']
    except Exception as e:
        logging.error(f"Error fetching policy document for {policy_arn}: {e}")
        return None

def analyze_statement(statement):
    """Analyze a single policy statement for violations"""
    violations = []
    
    # Skip Deny statements
    if statement.get('Effect') == 'Deny':
        return violations
    
    action = statement.get('Action', [])
    resource = statement.get('Resource', [])
    
    # Normalize to lists
    if not isinstance(action, list):
        action = [action]
    if not isinstance(resource, list):
        resource = [resource]
    
    # Check for full admin access
    if '*' in action and '*' in resource:
        violations.append('full_admin')
    
    # Check for wildcard actions
    elif '*' in action:
        violations.append('wildcard_actions')
    
    # Check for wildcard resources
    if '*' in resource and 'full_admin' not in violations:
        violations.append('wildcard_resources')
    
    # Check for overly broad service access (e.g., s3:*, ec2:*)
    for act in action:
        if isinstance(act, str) and act.endswith(':*') and act != '*':
            violations.append('overly_broad_service')
            break
    
    # Check for NotAction usage
    if 'NotAction' in statement:
        violations.append('notaction_usage')
    
    return violations

def analyze_policy(policy):
    """Analyze a policy for least-privilege violations"""
    policy_name = policy['PolicyName']
    policy_arn = policy['Arn']
    default_version_id = policy['DefaultVersionId']
    
    logging.info(f"Analyzing policy: {policy_name}")
    
    findings = []
    
    # Get policy document
    policy_doc = get_policy_document(policy_arn, default_version_id)
    if not policy_doc:
        return findings
    
    # Get statements
    statements = policy_doc.get('Statement', [])
    if not isinstance(statements, list):
        statements = [statements]
    
    # Analyze each statement
    all_violations = set()
    for statement in statements:
        violations = analyze_statement(statement)
        all_violations.update(violations)
    
    # Create findings for each violation
    for violation_type in all_violations:
        violation_info = VIOLATION_PATTERNS[violation_type]
        findings.append({
            'PolicyName': policy_name,
            'PolicyARN': policy_arn,
            'ViolationType': violation_info['name'],
            'Severity': violation_info['severity'],
            'Description': violation_info['description'],
            'Recommendation': f"Review and restrict permissions following least-privilege principle"
        })
        logging.warning(f"  - {violation_info['severity']}: {violation_info['name']}")
    
    return findings

def generate_report(findings):
    """Generate CSV report of findings"""
    if not findings:
        logging.info("No least-privilege violations found!")
        return
    
    logging.info(f"Found {len(findings)} violation(s). Generating report...")
    
    # Create DataFrame
    df = pd.DataFrame(findings)
    
    # Sort by severity
    severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    df['SeverityOrder'] = df['Severity'].map(severity_order)
    df = df.sort_values('SeverityOrder').drop('SeverityOrder', axis=1)
    
    # Generate report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = f'least_privilege_report_{timestamp}.csv'
    df.to_csv(report_path, index=False)
    
    logging.info(f"Report saved to: {report_path}")
    
    # Print summary
    print("\n" + "="*60)
    print("LEAST-PRIVILEGE COMPLIANCE SUMMARY")
    print("="*60)
    print(f"Total Violations: {len(findings)}")
    print(f"\nBy Severity:")
    for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        count = len(df[df['Severity'] == severity])
        if count > 0:
            print(f"  {severity}: {count}")
    print("="*60 + "\n")

def main():
    """Main execution function"""
    try:
        # Get all customer-managed policies
        policies = get_customer_managed_policies()
        
        if not policies:
            logging.info("No customer-managed policies found.")
            return
        
        # Analyze each policy
        all_findings = []
        for policy in policies:
            findings = analyze_policy(policy)
            all_findings.extend(findings)
        
        # Generate report
        generate_report(all_findings)
        
        logging.info("Analysis complete!")
        
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()