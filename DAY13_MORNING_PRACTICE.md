# Day 13 Morning Practice - IAM MFA Auditor

## 🎯 **Practice Goal:**
Understand how to audit IAM users for MFA (Multi-Factor Authentication) enforcement.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `iam-mfa-auditor`
4. Click on: `iam_mfa_auditor.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Get IAM Users (around line 20)**
```python
users = iam_client.list_users()['Users']
```
- Gets all IAM users in the account
- Lists user names and metadata

### **Section 2: Check MFA Status (around line 30)**
```python
mfa_devices = iam_client.list_mfa_devices(UserName=user_name)
if len(mfa_devices['MFADevices']) == 0:
    # No MFA enabled
```
- Checks if user has MFA device registered
- If no devices = MFA not enabled

### **Section 3: Report Non-Compliant Users (around line 50)**
```python
if not mfa_enabled:
    audit_findings.append(...)
```
- Records users without MFA
- Generates compliance report

## 🎯 **Key Concept to Understand:**

**What is MFA (Multi-Factor Authentication)?**
- Requires two or more forms of authentication
- Something you know (password) + something you have (code/token)
- Adds an extra layer of security

**Why is MFA Critical for IAM Users?**
- Passwords can be stolen or guessed
- MFA prevents unauthorized access even if password is compromised
- Required by most compliance standards (SOC 2, PCI-DSS, etc.)
- Reduces risk of account takeover

**Common MFA Methods:**
- Virtual MFA (Google Authenticator, Authy)
- Hardware tokens (YubiKey)
- SMS-based codes
- Biometric (fingerprint, face)

## 💡 **Morning Practice Task:**

1. Open `iam_mfa_auditor.py`
2. Find the MFA status check logic
3. Read through the code
4. Answer this question: **Why is MFA important for IAM users?**

## 🚀 **Answer:**
MFA adds an extra layer of security by requiring a second form of authentication beyond just a password. This prevents unauthorized access even if passwords are compromised, reduces the risk of account takeover, and is required by most compliance standards.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** Python, boto3, IAM, MFA, compliance auditing
