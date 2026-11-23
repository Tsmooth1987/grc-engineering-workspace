# Day 28 Morning Practice - CloudFormation Review

## 🎯 **Practice Goal:**
Review CloudFormation and understand Infrastructure as Code for AWS.

## 📂 **Step 1: Open CloudFormation Template**

1. Look at the file tree on the left
2. Find file: `s3-encryption-rule-template.yaml`
3. This is the CloudFormation template we created for the custom Config rule

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Template Header (around line 1)**
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Custom Config Rule for S3 Encryption Check'
```
- Template format version
- Description of what the template does
- Metadata for the stack

### **Section 2: Resources Block (around line 7)**
```yaml
Resources:
  ConfigRule:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: s3-bucket-encryption-check
```
- Defines AWS resources to create
- Resource type: AWS::Config::ConfigRule
- Resource name: ConfigRule
- Properties for the resource

### **Section 3: Lambda Function (around line 20)**
```yaml
LambdaFunction:
  Type: AWS::Lambda::Function
  Properties:
    FunctionName: s3-encryption-config-rule
    Runtime: python3.9
    Handler: index.lambda_handler
```
- Creates Lambda function
- Runtime: python3.9
- Handler: function name
- Inline code or S3 bucket reference

## 🎯 **Key Concept to Understand:**

**CloudFormation Core Concepts:**
- Template: YAML/JSON file describing infrastructure
- Stack: Collection of resources managed as a single unit
- Resources: AWS components (Lambda, S3, IAM, etc.)
- Parameters: Input values when creating stack
- Outputs: Values after stack creation

**CloudFormation vs Terraform:**
- CloudFormation: AWS-native, YAML/JSON, tight AWS integration
- Terraform: Multi-cloud, HCL language, popular with DevOps
- Both: Infrastructure as Code

**CloudFormation Benefits:**
- AWS-native with all features
- Built-in change sets for safety
- Drift detection
- Stack policies
- Cross-stack references

## 💡 **Morning Practice Task:**

1. Open `s3-encryption-rule-template.yaml`
2. Read through the YAML code
3. Understand the resource blocks
4. Answer this question: **Why would you choose CloudFormation over Terraform for AWS-only workloads?**

## 🚀 **Answer:**
CloudFormation is AWS-native and integrates tightly with all AWS services, often getting new features first. It has built-in change sets for safe deployments, drift detection, and requires no additional tooling since it's built into AWS.

---

**Time needed:** 10-15 minutes
**Difficulty:** Medium
**Skills:** CloudFormation, YAML, IaC, AWS infrastructure, stack management
