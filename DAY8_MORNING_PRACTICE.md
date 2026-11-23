# Day 8 Morning Practice - Multi-Account Security Hub Aggregator

## 🎯 **Practice Goal:**
Understand enterprise-scale security aggregation across multiple AWS accounts using STS cross-account access.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `multi-account-security-hub`
4. Click on: `lambda_function.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: STS Role Assumption (around line 30)**
```python
sts_client = boto3.client('sts')
assumed_role = sts_client.assume_role(
    RoleArn=role_arn,
    RoleSessionName='SecurityHubAggregation'
)
```
- Uses STS (Security Token Service) to assume a role in another account
- Cross-account access without storing credentials
- Temporary credentials

### **Section 2: Get Findings from Member Account (around line 50)**
```python
securityhub = boto3.client('securityhub', region_name=region, ...)
findings = securityhub.get_findings(...)
```
- Connects to Security Hub in member account
- Fetches security findings
- Aggregates across multiple accounts

### **Section 3: Centralized Reporting (around line 70)**
```python
all_findings.extend(member_findings)
```
- Combines findings from all accounts
- Single view of enterprise security posture
- Centralized management

## 🎯 **Key Concept to Understand:**

**What is Multi-Account Architecture?**
- Using multiple AWS accounts for different purposes
- Prod, dev, staging, workloads in separate accounts
- Better security isolation
- Easier compliance management

**What is STS Assume Role?**
- Temporary cross-account access
- No permanent credentials stored
- Automatic credential rotation
- Auditable access patterns

**Why Aggregate Security Hub?**
- Single view of security across all accounts
- Centralized security operations
- Consistent compliance reporting
- Efficient incident response

## 💡 **Morning Practice Task:**

1. Open `lambda_function.py` in multi-account-security-hub
2. Look at the STS role assumption code
3. Read the cross-account findings fetch logic
4. Answer this question: **Why is multi-account security aggregation important for enterprises?**

## 🚀 **Answer:**
Multi-account security aggregation provides a single view of security posture across all AWS accounts, enabling centralized security operations, consistent compliance reporting, and efficient incident response. It eliminates the need to check each account individually and provides enterprise-wide visibility.

---

**Time needed:** 10-15 minutes
**Difficulty:** Medium
**Skills:** Python, boto3, STS, cross-account access, Security Hub, enterprise architecture
