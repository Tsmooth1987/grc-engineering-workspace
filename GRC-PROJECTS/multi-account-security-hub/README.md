# Multi-Account Security Hub Aggregator

Enterprise-scale Lambda function for aggregating AWS Security Hub findings across multiple accounts with professional Excel reporting.

## 🎯 Overview

This serverless solution aggregates Security Hub findings from multiple AWS accounts into a single, formatted Excel report. Perfect for security teams managing multi-account AWS Organizations who need centralized compliance reporting.

## ✨ Features

- **Multi-Account Aggregation** - Collect findings from multiple AWS accounts
- **Serverless Architecture** - AWS Lambda for scalable, cost-effective execution
- **Excel Reporting** - Professional, formatted Excel reports with styling
- **S3 Integration** - Automatic report storage in S3
- **Cross-Account Access** - Uses STS AssumeRole for secure access
- **Automated Execution** - Can be triggered on schedule or on-demand
- **Comprehensive Logging** - CloudWatch Logs integration

## 🏗️ Architecture

## 🚀 Quick Start

### Prerequisites

- AWS Organizations with multiple accounts
- Security Hub enabled in all accounts
- IAM roles configured for cross-account access
- S3 bucket for report storage

---

## Quick Start

```bash
# Clone and deploy in 4 commands
git clone https://github.com/Tsmooth1987/multi-account-security-hub-aggregator.git
cd multi-account-security-hub-aggregator
aws cloudformation deploy --template-file management-account-stack.yaml --stack-name security-hub-aggregator --capabilities CAPABILITY_IAM
python lambda_function.py
```

**Prerequisites:** AWS Organizations, Security Hub enabled in all accounts, AWS CLI configured

---

## Step-by-Step Deployment

**1. Deploy Member Account Roles (in each member account):**
```bash
aws cloudformation create-stack \
  --stack-name security-hub-member-role \
  --template-body file://member-account-role.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters ParameterKey=ManagementAccountId,ParameterValue=YOUR_MGMT_ACCOUNT_ID