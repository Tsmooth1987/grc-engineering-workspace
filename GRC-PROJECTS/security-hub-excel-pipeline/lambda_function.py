"""
AWS Security Hub to Excel Report Generator
=========================================
Lambda function that fetches Security Hub findings and generates a professional Excel report.

Environment Variables Required:
- S3_BUCKET_NAME: S3 bucket to store the generated Excel reports

Author: Terence Webster
Date: 2026-11-19
Purpose: Automated Security Hub compliance reporting
"""

import json
import boto3
import logging
import os
from datetime import datetime
from io import BytesIO
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

# Configure logging for CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Main Lambda handler for Security Hub to Excel conversion.

    Workflow:
    1. Validate environment variables
    2. Initialize AWS clients (S3, Security Hub)
    3. Fetch active Security Hub findings using pagination
    4. Create Excel workbook with professional formatting
    5. Upload report to S3 with timestamp
    6. Return success response with report location

    Args:
        event: Lambda event (not used currently)
        context: Lambda context (not used currently)

    Returns:
        dict: HTTP response with status code and body
    """
    try:
        # Step 1: Validate environment configuration
        logger.info("=== Security Hub Excel Pipeline Started ===")
        bucket_name = os.environ.get('S3_BUCKET_NAME')
        
        if not bucket_name:
            error_msg = "S3_BUCKET_NAME environment variable not set"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        logger.info(f"Target S3 bucket: {bucket_name}")

        # Step 2: Initialize AWS clients
        logger.info("Initializing AWS clients...")
        s3 = boto3.client('s3')
        securityhub = boto3.client('securityhub')
        logger.info("AWS clients initialized successfully")

        # Step 3: Fetch Security Hub findings with pagination
        logger.info("Fetching Security Hub findings...")
        findings = []
        
        # Use paginator to handle large result sets
        paginator = securityhub.get_paginator('get_findings')
        
        # Filter for ACTIVE findings only (ignore ARCHIVED)
        filter_params = {
            'RecordState': [{'Value': 'ACTIVE', 'Comparison': 'EQUALS'}]
        }
        
        page_count = 0
        for page in paginator.paginate(Filters=filter_params):
            findings.extend(page['Findings'])
            page_count += 1
            logger.debug(f"Processed page {page_count}, total findings so far: {len(findings)}")
        
        logger.info(f"Total ACTIVE findings retrieved: {len(findings)}")
        
        if len(findings) == 0:
            logger.warning("No active Security Hub findings found")
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'No active findings to report',
                    'findings_count': 0
                })
            }

        # Step 4: Create Excel workbook with professional formatting
        logger.info("Creating Excel workbook...")
        wb = Workbook()
        ws = wb.active
        ws.title = "Security Hub Findings"
        
        # Define column headers
        headers = [
            'Title',
            'Severity',
            'Resource Type',
            'Resource ID',
            'Status',
            'Account',
            'Region'
        ]
        
        # Add header row with professional styling
        ws.append(headers)
        
        # Apply header formatting: bold white text on dark blue background
        header_fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
        header_font = Font(bold=True, color='FFFFFF')
        
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal='center', vertical='center')
        
        # Add findings data rows
        for finding in findings:
            # Safely extract nested data with fallback to 'N/A'
            resources = finding.get('Resources', [{}])
            resource = resources[0] if resources else {}
            
            ws.append([
                finding.get('Title', 'N/A'),
                finding.get('Severity', {}).get('Label', 'N/A'),
                resource.get('Type', 'N/A'),
                resource.get('Id', 'N/A'),
                finding.get('Compliance', {}).get('Status', 'N/A'),
                finding.get('AwsAccountId', 'N/A'),
                finding.get('Region', 'N/A')
            ])
        
        # Auto-adjust column widths for better readability
        for col in range(1, len(headers) + 1):
            ws.column_dimensions[get_column_letter(col)].width = 25
        
        logger.info(f"Excel workbook created with {len(findings)} rows")

        # Step 5: Save workbook to memory buffer
        logger.info("Saving workbook to buffer...")
        buffer = BytesIO()
        wb.save(buffer)
        buffer.seek(0)
        logger.info("Workbook saved to buffer successfully")

        # Step 6: Upload to S3 with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_key = f"reports/security_hub_{timestamp}.xlsx"
        
        logger.info(f"Uploading report to S3: s3://{bucket_name}/{report_key}")
        s3.put_object(
            Bucket=bucket_name,
            Key=report_key,
            Body=buffer.getvalue(),
            ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        logger.info(f"Report uploaded successfully to s3://{bucket_name}/{report_key}")
        logger.info("=== Security Hub Excel Pipeline Completed Successfully ===")

        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Report generated successfully',
                'report_key': report_key,
                'report_url': f"s3://{bucket_name}/{report_key}",
                'findings_count': len(findings),
                'timestamp': timestamp
            })
        }

    except ValueError as ve:
        # Handle configuration errors
        logger.error(f"Configuration error: {str(ve)}")
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Configuration error',
                'message': str(ve)
            })
        }
        
    except Exception as e:
        # Handle unexpected errors
        logger.error(f"Unexpected error in lambda_handler: {str(e)}", exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e)
            })
        }
