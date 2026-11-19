# AWS Security Hub Custom Controls - Deployment Guide

## 🚀 Deployment Instructions

### Prerequisites
- AWS CLI installed and configured
- Security Hub enabled in target AWS account
- CloudFormation permissions in target account
- Python 3.11+ (for local testing)

### Quick Deployment

```bash
# 1. Navigate to deployment directory
cd deployment

# 2. Make deployment script executable
chmod +x deploy.sh

# 3. Run deployment script
./deploy.sh
```

### Manual Deployment

```bash
# 1. Validate CloudFormation template
aws cloudformation validate-template --template-body file://deployment/template.yaml

# 2. Deploy CloudFormation stack
aws cloudformation deploy \
  --template-file deployment/template.yaml \
  --stack-name security-hub-custom-controls-dev \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    ProjectName=security-hub-custom-controls \
    Environment=dev \
    EnableMonitoring=true \
  --region us-east-1
```

## 📋 Deployment Components

### CloudFormation Stack Resources

1. **Lambda Function** (`CustomControlsLambda`)
   - Runtime: Python 3.11
   - Handler: custom_controls.custom_compliance_control.lambda_handler
   - Timeout: 300 seconds
   - Memory: 256 MB

2. **IAM Role** (`LambdaExecutionRole`)
   - Security Hub access (batch_import_findings, describe_hub)
   - S3 access (versioning, encryption, public access)
   - IAM access (get_user, get_login_profile, list_mfa_devices)
   - CloudWatch Logs access

3. **S3 Bucket** (`ControlOutputsBucket`)
   - Encryption: AES256
   - Versioning: Enabled
   - Public access: Blocked
   - Secure by default

4. **CloudWatch Monitoring**
   - Log group for Lambda function
   - Error alarm (5 errors in 5 minutes)
   - Duration alarm (60 seconds threshold)

### Deployment Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| ProjectName | security-hub-custom-controls | Project name for resource naming |
| Environment | dev | Deployment environment (dev/staging/prod) |
| EnableMonitoring | true | Enable CloudWatch monitoring |

## 🔧 Configuration

### Custom Compliance Rules

Edit the `_load_compliance_rules()` method in `deployment/lambda_function.py` to customize compliance requirements:

```python
def _load_compliance_rules(self) -> Dict[str, Any]:
    return {
        "s3_versioning": {
            "required": True,
            "description": "S3 buckets must have versioning enabled",
            "severity": "HIGH"
        },
        # Add your custom rules here
    }
```

### Resource Evaluation

Implement custom resource evaluation logic in the appropriate methods:

- `_evaluate_s3_bucket()`: S3 bucket security checks
- `_evaluate_iam_user()`: IAM user security checks
- Add new methods for additional resource types

## 🧪 Testing

### Local Testing

```bash
# Install dependencies
pip install boto3 pytest

# Run unit tests
pytest tests/

# Test Lambda function locally
python3 deployment/lambda_function.py
```

### CloudFormation Testing

```bash
# Validate template
aws cloudformation validate-template --template-body file://deployment/template.yaml

# Test deployment to dev environment
./deployment/deploy.sh
```

### Production Testing

```bash
# Deploy to staging
aws cloudformation deploy \
  --template-file deployment/template.yaml \
  --stack-name security-hub-custom-controls-staging \
  --parameter-overrides Environment=staging

# Test in staging environment
# Verify Security Hub integration
# Monitor CloudWatch logs

# Deploy to production
aws cloudformation deploy \
  --template-file deployment/template.yaml \
  --stack-name security-hub-custom-controls-prod \
  --parameter-overrides Environment=prod
```

## 📊 Monitoring

### CloudWatch Logs

```bash
# View Lambda logs
aws logs tail /aws/lambda/security-hub-custom-controls-dev --follow

# View specific log streams
aws logs tail /aws/lambda/security-hub-custom-controls-dev --follow --filter-pattern "ERROR"
```

### CloudWatch Alarms

The stack creates two CloudWatch alarms:

1. **Lambda Error Alarm**: Triggers on 5+ errors in 5 minutes
2. **Lambda Duration Alarm**: Triggers on average duration > 60 seconds

### Custom Metrics

Add custom CloudWatch metrics in the Lambda function:

```python
cloudwatch = boto3.client('cloudwatch')
cloudwatch.put_metric_data(
    Namespace='CustomControls',
    MetricData=[{
        'MetricName': 'ComplianceFindings',
        'Value': len(findings),
        'Unit': 'Count'
    }]
)
```

## 🔒 Security Considerations

### IAM Permissions

The Lambda function uses least-privilege IAM policies:
- Specific Security Hub permissions only
- S3 access limited to required operations
- IAM access limited to read operations
- No admin or excessive permissions

### S3 Security

- Server-side encryption enabled (AES256)
- Versioning enabled for audit trail
- Public access blocked
- Secure transport required
- Bucket policy denies unencrypted uploads

### Lambda Security

- VPC isolation (if required)
- Environment variables for configuration
- No hardcoded credentials
- Secrets management via AWS Secrets Manager (if needed)

## 🔄 Updates and Rollbacks

### Update Deployment

```bash
# Update Lambda function code
aws cloudformation deploy \
  --template-file deployment/template.yaml \
  --stack-name security-hub-custom-controls-dev \
  --capabilities CAPABILITY_IAM
```

### Rollback

```bash
# Rollback to previous version
aws cloudformation rollback-stack \
  --stack-name security-hub-custom-controls-dev \
  --rollback-reason "Rolling back due to issues"

# Or delete and redeploy
aws cloudformation delete-stack --stack-name security-hub-custom-controls-dev
./deployment/deploy.sh
```

## 📝 Troubleshooting

### Common Issues

**Issue**: Lambda function times out
**Solution**: Increase timeout in CloudFormation template

**Issue**: Security Hub access denied
**Solution**: Verify IAM role has Security Hub permissions

**Issue**: S3 access denied
**Solution**: Check S3 bucket policy and IAM permissions

**Issue**: CloudFormation deployment fails
**Solution**: Check CloudFormation events for specific error details

### Debug Mode

Enable debug logging by updating Lambda environment variables:

```bash
aws lambda update-function-configuration \
  --function-name security-hub-custom-controls-dev \
  --environment Variables={LOG_LEVEL=DEBUG}
```

## 🚀 Next Steps

1. Customize compliance rules for your organization
2. Implement additional resource evaluation logic
3. Integrate with Security Hub custom controls configuration
4. Set up automated testing pipeline
5. Configure alerts and notifications
6. Document custom controls for security team

## 📞 Support

For deployment issues:
- Check CloudFormation stack events
- Review CloudWatch logs
- Verify IAM permissions
- Consult AWS Security Hub documentation

---

**Deployment Guide Version**: 1.0
**Last Updated**: September 4, 2026