# GuardDuty Integration Guide

## 🎯 **Practice Goal:**
Understand GuardDuty and how to automate threat response.

## 📖 **What is GuardDuty?**

**AWS GuardDuty** is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity and unauthorized behavior.

**Key Features:**
- Machine learning-powered threat detection
- Analyzes AWS CloudTrail events, VPC Flow Logs, DNS logs
- Detects compromised instances, reconnaissance, cryptocurrency mining
- Automated remediation via Lambda
- Integrated with Security Hub

## 📂 **Step 1: Enable GuardDuty**

**In AWS Console:**
1. Search for "GuardDuty"
2. Click "Get Started"
3. Enable GuardDuty (free 30-day trial, then $1/region/million events)
4. Review detected findings

## 📖 **Step 2: Create Auto-Remediation Lambda**

Create `guardduty_remediator.py`:

```python
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Auto-remediate GuardDuty findings
    
    Supported findings:
    - Trojan.EC2BlackholeTrafficDestination
    - CryptoCurrency:EC2/BitcoinTool.B!DNS
    - UnauthorizedAccess:IAMUser/TorIPCaller
    """
    finding = event['detail']['findings'][0]
    finding_type = finding['type']
    finding_id = finding['id']
    
    logger.info(f"Processing GuardDuty finding: {finding_type}")
    
    if finding_type == 'Trojan.EC2BlackholeTrafficDestination':
        # Isolate EC2 instance
        instance_id = finding['resource']['instanceDetails']['instanceId']
        remediate_ec2_instance(instance_id, 'isolate')
        
    elif finding_type == 'CryptoCurrency:EC2/BitcoinTool.B!DNS':
        # Stop and investigate EC2 instance
        instance_id = finding['resource']['instanceDetails']['instanceId']
        remediate_ec2_instance(instance_id, 'stop')
        
    elif finding_type == 'UnauthorizedAccess:IAMUser/TorIPCaller':
        # Disable IAM user access keys
        user_arn = finding['resource']['accessKeyDetails']['accessKeyId']
        disable_iam_keys(user_arn)
    
    logger.info(f"Remediation complete for finding: {finding_id}")
    return {'status': 'remediated', 'finding_id': finding_id}

def remediate_ec2_instance(instance_id, action):
    """
    Remediate EC2 instance
    
    Actions:
    - isolate: Remove from security groups, add to quarantine SG
    - stop: Stop the instance
    """
    ec2 = boto3.client('ec2')
    
    if action == 'isolate':
        # Remove from all security groups
        ec2.modify_instance_attribute(
            InstanceId=instance_id,
            Groups=[]
        )
        # Add to quarantine security group (no ingress/egress)
        logger.info(f"Isolated instance: {instance_id}")
        
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=[instance_id])
        logger.info(f"Stopped instance: {instance_id}")

def disable_iam_keys(user_arn):
    """
    Disable IAM user access keys
    """
    iam = boto3.client('iam')
    user_name = user_arn.split('/')[-1]
    
    # List access keys
    keys = iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']
    
    for key in keys:
        if key['Status'] == 'Active':
            iam.disable_access_key(
                UserName=user_name,
                AccessKeyId=key['AccessKeyId']
            )
            logger.info(f"Disabled access key for user: {user_name}")
```

## 📖 **Step 3: Deploy with CloudFormation**

Create `guardduty-remediation-template.yaml`:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'GuardDuty Auto-Remediation'

Resources:
  RemediationLambda:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: guardduty-auto-remediator
      Runtime: python3.9
      Handler: guardduty_remediator.lambda_handler
      Code:
        ZipFile: |
          import json
          import boto3
          import logging
          
          logger = logging.getLogger()
          logger.setLevel(logging.INFO)
          
          def lambda_handler(event, context):
              finding = event['detail']['findings'][0]
              finding_type = finding['type']
              logger.info(f"Processing: {finding_type}")
              return {'status': 'processed', 'finding_id': finding['id']}
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
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
      Policies:
        - PolicyName: GuardDutyRemediation
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - ec2:ModifyInstanceAttribute
                  - ec2:StopInstances
                  - iam:ListAccessKeys
                  - iam:DisableAccessKey
                Resource: '*'

  GuardDutyEventRule:
    Type: AWS::Events::Rule
    Properties:
      Description: Trigger Lambda on GuardDuty findings
      EventPattern:
        source:
          - aws.guardduty
        detail-type:
          - GuardDuty Finding
      State: ENABLED
      Targets:
        - Arn: !GetAtt RemediationLambda.Arn

  LambdaPermission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !GetAtt RemediationLambda.Arn
      Action: lambda:InvokeFunction
      Principal: events.amazonaws.com
```

## 🎯 **Key Concepts:**

**GuardDuty Finding Types:**
- CryptoCurrency: Mining operations
- Trojan: Malware indicators
- UnauthorizedAccess: Suspicious access patterns
- Reconnaissance: Pre-attack behavior

**Auto-Remediation Actions:**
- Isolate: Remove network access
- Stop: Stop the resource
- Disable: Disable credentials
- Investigate: Tag for review

**EventBridge Integration:**
- Triggers Lambda on findings
- Real-time response
- Automated remediation

## 💡 **Practice Task:**

1. Enable GuardDuty in your AWS account
2. Review any detected findings
3. Deploy the remediation Lambda
4. Test the automation

## 🚀 **Advanced Next Steps:**

- Add SNS notifications for critical findings
- Create custom GuardDuty filters
- Integrate with ServiceNow or Jira
- Build custom threat intelligence rules

---

**Time needed:** 30-45 minutes
**Difficulty:** Medium
**Skills:** GuardDuty, Lambda, EventBridge, EC2, IAM, threat response
