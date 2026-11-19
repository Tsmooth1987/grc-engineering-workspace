"""
Multi-Account Security Hub Aggregator - Simplified Version
Author: Terence Webster - Project 9
"""

import json
import boto3
import logging
from datetime import datetime
from io import BytesIO
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')
sts_client = boto3.client('sts')


def lambda_handler(event, context):
    """Main handler - simplified for single account"""
    try:
        logger.info("Starting Security Hub aggregation")
        
        import os
        bucket_name = os.environ.get('S3_BUCKET_NAME')
        
        if not bucket_name:
            raise ValueError("S3_BUCKET_NAME not set")
        
        # Get findings from current account
        sh_client = boto3.client('securityhub')
        findings = []
        
        paginator = sh_client.get_paginator('get_findings')
        filters = {'RecordState': [{'Value': 'ACTIVE', 'Comparison': 'EQUALS'}]}
        
        for page in paginator.paginate(Filters=filters, MaxResults=100):
            findings.extend(page['Findings'])
        
        logger.info(f"Retrieved {len(findings)} findings")
        
        # Generate Excel report
        excel_buffer = generate_report(findings)
        
        # Upload to S3
        report_key = f"reports/multi_account_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        s3_client.put_object(
            Bucket=bucket_name,
            Key=report_key,
            Body=excel_buffer.getvalue(),
            ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        logger.info(f"Report uploaded to s3://{bucket_name}/{report_key}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Report generated successfully',
                'findings_count': len(findings),
                's3_key': report_key
            })
        }
        
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


def generate_report(findings):
    """Generate Excel report"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Security Hub Findings"
    
    # Headers
    headers = ['Title', 'Severity', 'Resource Type', 'Resource ID', 'Status', 'Account', 'Region']
    ws.append(headers)
    
    for col in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col)
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
    
    # Data
    for finding in findings:
        resources = finding.get('Resources', [{}])
        ws.append([
            finding.get('Title', 'N/A'),
            finding.get('Severity', {}).get('Label', 'N/A'),
            resources[0].get('Type', 'N/A'),
            resources[0].get('Id', 'N/A'),
            finding.get('Compliance', {}).get('Status', 'N/A'),
            finding.get('AwsAccountId', 'N/A'),
            finding.get('Region', 'N/A')
        ])
    
    # Column widths
    for col in range(1, len(headers) + 1):
        ws.column_dimensions[get_column_letter(col)].width = 25
    
    # Save to buffer
    excel_buffer = BytesIO()
    wb.save(excel_buffer)
    excel_buffer.seek(0)
    
    return excel_buffer