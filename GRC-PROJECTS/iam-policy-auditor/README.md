# IAM Policy Auditor

Detect overly permissive IAM policies with full administrator access in your AWS account.

## 🎯 Overview

This tool audits all customer-managed IAM policies in your AWS account to identify policies that grant full administrator access (`Allow`, `*`, `*`). This helps identify security risks and ensure least-privilege access.

## ✨ Features

- **Admin Policy Detection** - Identifies policies with full `*:*` permissions
- **Customer-Managed Focus** - Audits only your custom policies, not AWS-managed ones
- **CSV Reporting** - Generates detailed audit reports
- **Comprehensive Logging** - Tracks all analysis operations
- **Pattern Matching** - Detects the specific high-risk permission pattern

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- AWS CLI configured with appropriate credentials
- IAM permissions to list and read policies

### Installation

```bash
# Clone and run in 3 commands
git clone https://github.com/Tsmooth1987/iam-policy-auditor.git
cd iam-policy-auditor
pip install -r requirements.txt
python iam_policy_auditor.py