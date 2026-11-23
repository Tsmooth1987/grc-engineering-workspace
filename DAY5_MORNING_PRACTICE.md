# Day 5 Morning Practice - Least-Privilege Compliance Checker

## 🎯 **Practice Goal:**
Understand advanced IAM policy analysis detecting multiple types of least-privilege violations.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `least-privilege-checker`
4. Click on: `least_privilege_checker.py`

## 📖 **Step 2: Read the Code (15-20 minutes)**

Look for these key sections:

### **Section 1: Multiple Violation Types (around line 30)**
This checker detects 5 types of violations:
1. Full admin access (Allow, *, *)
2. Wildcard actions (Allow, *, specific_resource)
3. Wildcard resources (Allow, specific_action, *)
4. Service-wide access (Allow, service:*, specific_resource)
5. Management-level access (Access to IAM/Security services)

### **Section 2: Severity Classification (around line 60)**
```python
if violation_type == 'FULL_ADMIN':
    severity = 'HIGH'
elif violation_type == 'WILDCARD_ACTIONS':
    severity = 'MEDIUM'
```
- Classifies violations by severity
- HIGH = Most dangerous
- MEDIUM = Moderate risk
- LOW = Lower risk

### **Section 3: Recommendations (around line 80)**
```python
recommendations = {
    'FULL_ADMIN': 'Remove this policy immediately. Use specific permissions instead.',
    'WILDCARD_ACTIONS': 'Specify exact actions needed. Avoid using * for actions.'
}
```
- Provides actionable remediation steps
- Helps fix the security issue

## 🎯 **Key Concept to Understand:**

**What is Least Privilege?**
- Security principle: Give users only the permissions they need
- Not more, not less
- Reduces risk if account is compromised

**Why is wildcard (*) dangerous?**
- `Action: *` = Can do ANY action
- `Resource: *` = Can access ANY resource
- Too much permission = high risk

**Severity Levels:**
- **HIGH** = Immediate action required
- **MEDIUM** = Fix within reasonable time
- **LOW** = Address when convenient

## 💡 **Morning Practice Task:**

1. Open `least_privilege_checker.py`
2. Look at the 5 violation types it detects
3. Read the severity classification logic
4. Answer this question: **Why is the least-privilege principle important for security?**

## 🚀 **Answer:**
The least-privilege principle minimizes the potential damage from compromised accounts by ensuring users only have access to what they need. If an account is hacked, the attacker can only do what that account is authorized to do, limiting the blast radius and reducing overall security risk.

---

**Time needed:** 15-20 minutes
**Difficulty:** Medium
**Skills:** Python, boto3, IAM, JSON parsing, security analysis, severity classification
