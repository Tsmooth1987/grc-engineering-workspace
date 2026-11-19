# EC2 Security Group Auditor

A Python script to audit AWS EC2 security groups for security best practices and compliance.

## Features

- Identifies security groups with overly permissive rules
- Finds unused security groups
- Checks for public access to sensitive ports
- Generates detailed reports in CSV or JSON format
- Supports filtering by VPC and severity level

## Prerequisites

- Python 3.6+
- AWS CLI configured with appropriate credentials
- Required Python packages (install via `pip install -r requirements.txt`)

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python sg_auditor.py --profile your_profile_name
```

### Command Line Options

```
--profile TEXT     AWS profile name (default: default)
--region TEXT      AWS region (default: us-east-1)
--output [csv|json] Output format (default: csv)
--report FILE      Save report to file (default: security_group_audit_<timestamp>.<format>)
--vpc-id TEXT      Only check security groups in this VPC
--severity [low|medium|high|critical]  Minimum severity to report (default: low)
--verbose          Show detailed output
--debug            Enable debug mode
```

### Examples

1. Run audit in a specific region:
   ```bash
   python sg_auditor.py --profile production --region us-west-2
   ```

2. Generate JSON report:
   ```bash
   python sg_auditor.py --profile dev --output json
   ```

3. Check only critical issues in a specific VPC:
   ```bash
   python sg_auditor.py --profile test --vpc-id vpc-12345678 --severity critical
   ```

## Report Interpretation

### Severity Levels

- **Critical**: Public access to sensitive ports (SSH, RDP, databases)
- **High**: Unrestricted access to non-standard ports
- **Medium**: Overly broad IP ranges
- **Low**: Unused security groups, informational findings

### Report Fields

- `severity`: Issue severity level
- `group_id`: Security group ID
- `group_name`: Security group name
- `issue_type`: Type of issue found
- `vpc_id`: VPC ID where the security group resides
- Additional fields with details about the specific finding

## Security Best Practices

1. Review all critical findings immediately
2. Restrict access to sensitive ports (e.g., 22, 3389, 1433) to specific IP ranges
3. Remove or clean up unused security groups
4. Schedule regular audits using this tool
5. Implement the principle of least privilege for all security group rules

## License

This project is licensed under the MIT License - see the LICENSE file for details.
