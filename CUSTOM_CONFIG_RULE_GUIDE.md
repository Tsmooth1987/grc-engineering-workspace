# Build Custom AWS Config Rule - Simple S3 Encryption Check

## 🎯 **Practice Goal:**
Create a simple custom AWS Config rule using Python to check S3 bucket encryption.

## 📂 **Prerequisites:**

1. AWS CLI configured
2. Python 3.8+ installed
3. AWS Config already enabled in your account
4. pip install boto3

## 📖 **Step 1: Create the Rule File**

Create a new file: `s3_encryption_config_rule.py`

```python
import json
import boto3

def evaluate_compliance(configuration, rule_parameters):
    """
    Evaluates S3 bucket encryption compliance
    
    Args:
        configuration: S3 bucket configuration
        rule_parameters: Rule parameters (not used in this simple example)
    
    Returns:
        Compliance evaluation result
    """
    resource_id = configuration['resourceId']
    bucket_name = resource_id.split('/')[-1]
    
    s3 = boto3.client('s3')
    
    try:
        # Check if bucket has encryption enabled
        encryption = s3.get_bucket_encryption(Bucket=bucket_name)
        
        if 'ServerSideEncryptionConfiguration' in encryption:
            return {
                'compliance_type': 'COMPLIANT',
                'annotation': 'S3 bucket has encryption enabled'
            }
        else:
            return {
                'compliance_type': 'NON_COMPLIANT',
                'annotation': 'S3 bucket does not have encryption enabled'
            }
    except s3.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
            return {
                'compliance_type': 'NON_COMPLIANT',
                'annotation': 'S3 bucket encryption not configured'
            }
        else:
            return {
                'compliance_type': 'INSUFFICIENT_DATA',
                'annotation': f'Error checking encryption: {str(e)}'
            }

def lambda_handler(event, context):
    """
    AWS Lambda handler for Config rule
    
    Args:
        event: Config rule execution event
        context: Lambda context
    
    Returns:
        Evaluation results
    """
    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event['configurationItem']
    
    result = evaluate_compliance(configuration_item, event.get('ruleParameters', {}))
    
    return {
        'compliance_type': result['compliance_type'],
        'annotation': result['annotation'],
        'compliance_resource_id': configuration_item['resourceId'],
        'compliance_resource_type': configuration_item['resourceType']
    }
```

## 📖 **Step 2: Deploy with CloudFormation**

Create a CloudFormation template: `s3-encryption-rule-template.yaml`

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Custom Config Rule for S3 Encryption'

Resources:
  ConfigRule:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: s3-bucket-encryption-check
      Description: Checks if S3 buckets have encryption enabled
      Scope:
        ComplianceResourceTypes:
          - AWS::S3::Bucket
      Source:
        Owner: CUSTOM_LAMBDA
        SourceIdentifier: !GetAtt LambdaFunction.Arn
        SourceDetails:
          - EventSource: aws.config
            MessageType: ConfigurationItemChangeNotification

  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: s3-encryption-config-rule
      Runtime: python3.9
      Handler: s3_encryption_config_rule.lambda_handler
      Code:
        ZipFile: |
          import json
          import boto3
          
          def evaluate_compliance(configuration, rule_parameters):
              resource_id = configuration['resourceId']
              bucket_name = resource_id.split('/')[-1]
              s3 = boto3.client('s3')
              
              try:
                  encryption = s3.get_bucket_encryption(Bucket=bucket_name)
                  if 'ServerSideEncryptionConfiguration' in encryption:
                      return {
                          'compliance_type': 'COMPLIANT',
                          'annotation': 'S3 bucket has encryption enabled'
                      }
                  else:
                      return {
                          'compliance_type': 'NON_COMPLIANT',
                          'annotation': 'S3 bucket does not have encryption enabled'
                      }
              except Exception as e:
                  return {
                      'compliance_type': 'INSUFFICIENT_DATA',
                      'annotation': f'Error: {str(e)}'
                  }
          
          def lambda_handler(event, context):
              invoking_event = json.loads(event['invokingEvent'])
              configuration_item = invoking_event['configurationItem']
              result = evaluate_compliance(configuration_item, event.get('ruleParameters', {}))
              return {
                  'compliance_type': result['compliance_type'],
                  'annotation': result['annotation'],
                  'compliance_resource_id': configuration_item['resourceId'],
                  'compliance_resource_type': configuration_item['resourceType']
              }
      Role: !GetAtt LambdaRole.Arn
      Timeout: 30

  LambdaRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSConfigRulesExecutionRole
      Policies:
        - PolicyName: S3Access
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetBucketEncryption
                Resource: '*'

  LambdaPermission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !GetAtt LambdaFunction.Arn
      Action: lambda:InvokeFunction
      Principal: config.amazonaws.com
```

## 📖 **Step 3: Deploy**

```bash
aws cloudformation create-stack \
  --stack-name s3-encryption-config-rule \
  --template-body file://s3-encryption-rule-template.yaml \
  --capabilities CAPABILITY_IAM
```

## 🎯 **Key Concepts:**

**Config Rule Types:**
- Periodic: Runs on a schedule
- Trigger-based: Runs when resource changes (used here)

**Compliance Types:**
- COMPLIANT: Meets requirements
- NON_COMPLIANT: Does not meet requirements
- INSUFFICIENT_DATA: Cannot determine compliance

**CloudFormation Deployment:**
- Automates infrastructure setup
- Reproducible deployments
- Easy to manage updates

## 💡 **Practice Task:**

1. Create the CloudFormation template
2. Deploy to your AWS account
3. Check Config console for the new rule
4. Verify it evaluates S3 buckets

## 🚀 **Advanced Next Steps:**

- Add parameters for encryption type (AES256 vs aws:kms)
- Create remediation actions
- Add SNS notifications for non-compliant resources
- Build more complex rules for other services

---

**Time needed:** 30-45 minutes
**Difficulty:** Medium
**Skills:** Python, CloudFormation, AWS Config, Lambda, IAM
