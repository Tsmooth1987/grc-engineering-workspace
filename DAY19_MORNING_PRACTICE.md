# Day 19 Morning Practice - IAM Policy Auditor Deep Dive

## 🎯 **Practice Goal:**
Deep dive into IAM Policy Auditor to understand policy analysis and permission auditing.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `iam-policy-auditor`
4. Click on: `iam_policy_auditor.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Get IAM Policies (around line 25)**
```python
response = iam_client.list_policies(Scope='Local')
policies = response['Policies']
```
- Gets customer-managed policies only
- Filters out AWS-managed policies
- Focuses on your custom policies

### **Section 2: Policy Document Retrieval (around line 50)**
```python
version_response = iam_client.get_policy_version(
    PolicyArn=policy_arn,
    VersionId=default_version_id
)
```
- Gets the actual policy document
- Retrieves the default version
- Contains the permission statements

### **Section 3: Admin Access Check (around line 65)**
```python
is_admin_access = (
    statement.get('Effect') == 'Allow' and
    statement.get('Action') == '*' and
    statement.get('Resource') == '*'
)
```
- Checks for full admin access
- Dangerous pattern: Allow + '*' + '*'
- Most critical security risk

## 🎯 **Key Concept to Understand:**

**IAM Policy Structure:**
- Version: Which version of the policy
- Statement: Permission statements
- Effect: Allow or Deny
- Action: What AWS service/action
- Resource: What resource it applies to

**Admin Access Pattern:**
- Action: '*' = All actions
- Resource: '*' = All resources
- Effect: Allow = Permission granted
- This = Full administrator access

**Scope Filtering:**
- Local: Customer-managed policies
- AWS: AWS-managed policies
- Important distinction for auditing

## 💡 **Morning Practice Task:**

1. Open `iam_policy_auditor.py`
2. Look at the admin access check
3. Read the policy document retrieval
4. Answer this question: **Why is the pattern 'Allow + Action:* + Resource:*' dangerous?**

## 🚀 **Answer:**
The pattern 'Allow + Action:* + Resource:*' grants full administrator access to all AWS services and all resources. This is extremely dangerous because if the account is compromised, an attacker can do anything in the AWS account, including deleting resources, stealing data, and creating new users.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** Python, boto3, IAM, policy analysis, security auditing
