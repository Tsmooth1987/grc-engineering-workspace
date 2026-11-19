# S3 Auto-Remediator

Automatically audit and remediate S3 bucket security configurations across your AWS account.

## 🎯 Overview

This tool audits all S3 buckets in your AWS account for security compliance and automatically enables versioning on non-compliant buckets. It includes a dry-run mode for safe testing before making changes.

## ✨ Features

- **Automated Versioning Remediation** - Automatically enables versioning on buckets that don't have it
- **Dry-Run Mode** - Test the script safely without making any changes
- **Public Access Auditing** - Checks if public access block is configured
- **CSV Reporting** - Generates detailed compliance reports
- **Comprehensive Logging** - Logs all actions to file and console
- **Error Handling** - Gracefully handles AWS API errors

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- AWS CLI configured with appropriate credentials
- IAM permissions for S3 operations

### Installation

```bash
# Clone the repository
git clone [https://github.com/Tsmooth1987/s3-auto-remediator.git](https://github.com/Tsmooth1987/s3-auto-remediator.git)
cd s3-auto-remediator

# Install dependencies
pip install -r requirements.txt