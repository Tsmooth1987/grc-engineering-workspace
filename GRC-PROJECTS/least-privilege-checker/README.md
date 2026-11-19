# AWS Least-Privilege Compliance Checker

Advanced IAM policy analyzer that detects least-privilege violations and overly broad permissions across your AWS account.

## 🎯 Overview

This tool goes beyond basic admin access detection to identify multiple types of least-privilege violations in IAM policies. It provides severity-based findings with actionable recommendations for improving your security posture.

## ✨ Features

- **Multi-Pattern Detection** - Identifies 5 types of least-privilege violations
- **Severity Classification** - CRITICAL, HIGH, MEDIUM severity ratings
- **Comprehensive Analysis** - Analyzes all customer-managed IAM policies
- **Detailed Reporting** - CSV reports with recommendations
- **Summary Dashboard** - Console output with violation counts by severity
- **Professional Logging** - Audit trail of all analysis operations

## 🔍 Violation Types Detected

### CRITICAL
- **Full Administrator Access** - Policies with `Allow *:*` on all resources

### HIGH
- **Wildcard Actions** - Policies using `*` for actions
- **Wildcard Resources** - Policies using `*` for resources

### MEDIUM
- **Overly Broad Service Access** - Full service access (e.g., `s3:*`, `ec2:*`)
- **NotAction Usage** - Policies using NotAction which can be overly permissive

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- AWS CLI configured with appropriate credentials
- IAM permissions to read policies

### Installation

```bash
# Clone the repository
git clone [https://github.com/Tsmooth1987/least-privilege-checker.git](https://github.com/Tsmooth1987/least-privilege-checker.git)
cd least-privilege-checker

# Install dependencies
pip3 install -r requirements.txt --break-system-packages