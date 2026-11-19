# GRC Automation Projects

Complete collection of professional GRC (Governance, Risk, and Compliance) automation tools for AWS.

## 📋 Project Catalog

### 1. AI Risk Assessment Tool
**Purpose:** ISO/IEC 42001 AI system risk assessment with automated Excel reporting
**Skills:** Python, pandas, openpyxl, ISO/IEC 42001 controls
**Status:** Complete with GitHub repository

### 2. Security Hub Excel Pipeline
**Purpose:** Serverless Lambda function to extract Security Hub findings and generate Excel reports
**Skills:** AWS Lambda, Security Hub, CloudFormation, S3, openpyxl
**Status:** Complete - processed 140+ findings
**GitHub:** https://github.com/Tsmooth1987/aws-security-hub-excel-pipeline

### 3. Multi-Account Security Hub Aggregator
**Purpose:** Enterprise-scale multi-account security aggregation with cross-account IAM
**Skills:** Security Hub, STS, Organizations, Lambda, multi-account architecture
**Status:** Complete - processed 446 findings
**GitHub:** https://github.com/Tsmooth1987/multi-account-security-hub-aggregator

### 4. Security Hub Custom Controls
**Purpose:** Custom Security Hub controls beyond standard FSBP/CIS benchmarks
**Skills:** Security Hub custom controls, CloudFormation, Lambda, compliance logic
**Status:** Complete with deployment infrastructure
**GitHub:** https://github.com/Tsmooth1987/grc-security-hub-custom-controls

### 5. Least-Privilege Compliance Checker
**Purpose:** Advanced IAM policy analyzer detecting 5 types of least-privilege violations
**Skills:** boto3 (IAM), pandas, JSON parsing, security analysis
**Status:** Complete - detected HIGH severity violations in production
**GitHub:** https://github.com/Tsmooth1987/least-privilege-checker

### 6. IAM Policy Auditor
**Purpose:** Audits custom IAM policies for full administrator access (Allow, *, *)
**Skills:** boto3 (IAM), pandas, multi-step API calls, JSON parsing
**Status:** Complete

### 7. IAM MFA Auditor
**Purpose:** Audits IAM users for MFA enforcement compliance
**Skills:** boto3 (IAM), pandas, logging, AWS CLI
**Status:** Complete with full development lifecycle

### 8. EC2 Security Auditor
**Purpose:** Audits EC2 security groups for risky rules (SSH open to world)
**Skills:** boto3 (EC2), pandas, JSON parsing, security group analysis
**Status:** Complete

### 9. S3 Auto-Remediator
**Purpose:** Automatically enables versioning on non-compliant S3 buckets
**Skills:** boto3 (S3 write operations), argparse, safety features
**Status:** Complete with --dry-run mode

### 10. EBS Volume Remediator
**Purpose:** Deletes old, unattached EBS volumes for cost and security optimization
**Skills:** boto3 (EC2), pandas, logging, professional automation
**Status:** Complete with --dry-run mode

### 11. GRC Alerter
**Purpose:** Integrates auditors with AWS SNS for email alerting
**Skills:** boto3 (SNS), multi-service integration, event-driven automation
**Status:** Complete

## 🚀 Quick Start

Each project has its own README with setup instructions. Common setup:

```bash
# Navigate to project
cd GRC-PROJECTS/[project-name]

# Check for README
cat README.md

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure

# Run the tool
python [script-name].py
```

## 📊 Metrics

- **Total Projects:** 11
- **Lines of Code:** 5,000+
- **AWS Services Used:** 10+
- **Compliance Standards:** ISO 27001, ISO/IEC 42001, NIST, CIS
- **Production Deployments:** 3

## 🎯 Career Focus

These projects demonstrate expertise in:
- **Cloud Security Automation** - Automated compliance scanning and remediation
- **Serverless Architecture** - Lambda-based scalable solutions
- **Enterprise Security** - Multi-account security aggregation
- **Compliance Engineering** - Automated compliance at scale
- **Risk Assessment** - AI governance and security risk analysis

## 📈 Portfolio Integration

All major projects are deployed to GitHub and featured on:
- Portfolio Website: https://terence-webster.com
- GitHub: https://github.com/Tsmooth1987
