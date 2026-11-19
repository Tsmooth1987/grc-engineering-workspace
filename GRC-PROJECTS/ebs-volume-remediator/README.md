# EBS Volume Remediator

Identify and remove unattached EBS volumes to optimize costs and improve security.

## 🎯 Overview

This tool scans your AWS account for unattached EBS volumes and optionally deletes volumes older than 30 days. It helps reduce unnecessary AWS costs and maintains a clean infrastructure.

## ✨ Features

- **Unattached Volume Detection** - Finds all EBS volumes not attached to instances
- **Age-Based Filtering** - Identifies volumes older than 30 days
- **Dry-Run Mode** - Test safely without deleting anything
- **CSV Reporting** - Generates detailed reports with timestamps
- **Cost Optimization** - Reduces unnecessary storage costs
- **Comprehensive Logging** - Tracks all operations

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- AWS CLI configured with appropriate credentials
- IAM permissions for EC2 operations

### Installation

```bash
# Clone the repository
git clone [https://github.com/Tsmooth1987/ebs-volume-remediator.git](https://github.com/Tsmooth1987/ebs-volume-remediator.git)
cd ebs-volume-remediator

# Install dependencies
pip install -r requirements.txt