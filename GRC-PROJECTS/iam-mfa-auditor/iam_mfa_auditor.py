# --- IAM MFA Auditor ---

# This script will audit all IAM users in the account to check if they have
# Multi-Factor Authentication (MFA) enabled.
# It will then generate a CSV report of the findings.


# --- Step 1: Import Libraries and Set Up ---
import boto3
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('iam_mfa_auditor.log'), # Log to a file
        logging.StreamHandler() # Also log to the console
    ]
)

logging.info("IAM MFA Auditor script started.")


# --- Step 2: Get User List from AWS ---
iam_client = boto3.client('iam')
audit_results = [] # This list will hold our findings
users = [] # This will hold the user list from AWS

try:
    logging.info("Connecting to AWS to get IAM user list...")
    # The list_users call might need to be paginated for accounts with many users,
    # but for this exercise, we'll assume a single call is enough.
    response = iam_client.list_users()
    users = response.get('Users', [])
    logging.info(f"Successfully found {len(users)} users to audit.")
except Exception as e:
    logging.error(f"An error occurred while fetching the user list: {e}")


# --- Step 3: Loop Through Users and Check for MFA ---
if users:
    logging.info("Starting MFA audit for each user...")
    for user in users:
        user_name = user['UserName']
        mfa_enabled = False # Assume MFA is disabled unless we find a device

        try:
            # Check for MFA devices for the current user
            mfa_response = iam_client.list_mfa_devices(UserName=user_name)
            
            # If the 'MFADevices' list is not empty, the user has MFA enabled.
            if mfa_response.get('MFADevices'):
                mfa_enabled = True

            logging.info(f"  - User: '{user_name}', MFA Enabled: {mfa_enabled}")

            # Store the result
            audit_results.append({
                'UserName': user_name,
                'MFA_Enabled': mfa_enabled
            })

        except Exception as e:
            logging.error(f"Could not check MFA status for user '{user_name}'. Error: {e}")

    logging.info("Finished auditing all users.")


# --- Step 4: Create and Save the Report ---
if audit_results:
    logging.info("Creating CSV report from MFA audit findings...")
    try:
        df = pd.DataFrame(audit_results)
        report_path = 'iam_mfa_report.csv'
        df.to_csv(report_path, index=False)
        logging.info(f"Successfully saved MFA report to {report_path}")
    except Exception as e:
        logging.error(f"Could not save the MFA report. Error: {e}")
else:
    logging.warning("No audit results to save to a report.")


logging.info("IAM MFA Auditor script finished.")
