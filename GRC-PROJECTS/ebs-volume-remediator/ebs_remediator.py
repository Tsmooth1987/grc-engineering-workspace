import boto3
import pandas as pd
import logging
import argparse
from datetime import datetime, timedelta, timezone

# --- Configuration ---
# Configure the region to scan. For a real-world script, you might make this
# a command-line argument or read it from a config file.
AWS_REGION = "us-east-1"
REPORT_NAME = f"ebs_remediation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
LOG_FILE = "ebs_remediator.log"
DELETE_OLDER_THAN_DAYS = 30

# --- Logger Setup ---
def setup_logger(log_file):
    """Configures a logger to output to a file and the console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

# --- Main Logic ---
def get_unattached_volumes(ec2_client):
    """Scans for and returns a list of unattached EBS volumes."""
    unattached_volumes = []
    logging.info("Fetching all EBS volumes...")
    
    # We can use a paginator for APIs that return lists of items that might
    # span multiple pages. This is more robust than a simple list_volumes call.
    paginator = ec2_client.get_paginator('describe_volumes')
    pages = paginator.paginate(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )

    for page in pages:
        unattached_volumes.extend(page['Volumes'])

    if unattached_volumes:
        logging.info(f"Found {len(unattached_volumes)} unattached volume(s).")
    else:
        logging.info("No unattached EBS volumes found.")
        
    return unattached_volumes

def delete_volumes(ec2_client, volumes_to_delete, dry_run=True):
    """Deletes the specified EBS volumes, respecting the dry_run flag."""
    if not volumes_to_delete:
        logging.info("No volumes marked for deletion.")
        return

    if dry_run:
        logging.warning("--- DRY RUN MODE ENABLED: No volumes will be deleted. ---")
        for vol in volumes_to_delete:
            logging.info(f"DRY RUN: Would delete volume {vol['VolumeId']} (Size: {vol['Size']}GB, Created: {vol['CreateTime']}).")
        logging.warning("--- END DRY RUN MODE ---")
        return

    logging.info("--- Starting EBS Volume Deletion ---")
    for vol in volumes_to_delete:
        try:
            logging.info(f"Deleting volume {vol['VolumeId']}...")
            ec2_client.delete_volume(VolumeId=vol['VolumeId'])
            logging.info(f"Successfully deleted volume {vol['VolumeId']}.")
        except Exception as e:
            logging.error(f"Failed to delete volume {vol['VolumeId']}. Reason: {e}")
    logging.info("--- EBS Volume Deletion Finished ---")

def generate_report(volumes, report_name):
    """Generates a CSV report of the unattached volumes."""
    if not volumes:
        logging.info("No volumes to report.")
        return

    logging.info("Processing volume data for the report...")
    report_data = []
    for vol in volumes:
        report_data.append({
            'VolumeId': vol['VolumeId'],
            'Size': vol['Size'],
            'VolumeType': vol['VolumeType'],
            'CreateTime': vol['CreateTime'].strftime('%Y-%m-%d %H:%M:%S'),
            'AvailabilityZone': vol['AvailabilityZone']
        })
    
    # Create a pandas DataFrame
    df = pd.DataFrame(report_data)

    # Save the DataFrame to a CSV file
    logging.info(f"Generating CSV report: {report_name}")
    df.to_csv(report_name, index=False)
    logging.info("Report successfully generated.")

def main():
    """Main function to run the EBS volume remediator."""
    parser = argparse.ArgumentParser(description="Find and optionally delete old, unattached EBS volumes.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without deleting any volumes.")
    args = parser.parse_args()

    setup_logger(LOG_FILE)
    logging.info("--- Starting EBS Volume Remediator ---")
    if args.dry_run:
        logging.warning("Running in DRY RUN mode.")

    try:
        ec2_client = boto3.client('ec2', region_name=AWS_REGION)
        unattached_volumes = get_unattached_volumes(ec2_client)

        if not unattached_volumes:
            logging.info("No further action needed.")
            return

        generate_report(unattached_volumes, REPORT_NAME)

        # Identify volumes old enough to be deleted
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=DELETE_OLDER_THAN_DAYS)
        volumes_to_delete = [
            vol for vol in unattached_volumes 
            if vol['CreateTime'] < cutoff_date
        ]

        logging.info(f"Found {len(volumes_to_delete)} volumes older than {DELETE_OLDER_THAN_DAYS} days to be considered for deletion.")
        
        delete_volumes(ec2_client, volumes_to_delete, dry_run=args.dry_run)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    logging.info("--- EBS Volume Remediator Finished ---")

# --- Execution ---
if __name__ == "__main__":
    main()
