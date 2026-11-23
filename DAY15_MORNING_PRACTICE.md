# Day 15 Morning Practice - Least-Privilege Checker Deep Dive

## 🎯 **Practice Goal:**
Deep dive into the Least-Privilege Compliance Checker to understand severity classification and remediation recommendations.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `least-privilege-checker`
4. Click on: `least_privilege_checker.py`

## 📖 **Step 2: Read the Code (15-20 minutes)**

Look for these key sections:

### **Section 1: Violation Patterns (around line 30)**
```python
VIOLATION_PATTERNS = {
    'full_admin': {'severity': 'CRITICAL', ...},
    'wildcard_actions': {'severity': 'HIGH', ...},
    'wildcard_resources': {'severity': 'HIGH', ...},
    'overly_broad_service': {'severity': 'MEDIUM', ...},
    'notaction_usage': {'severity': 'MEDIUM', ...}
}
```
- 5 different violation types
- 3 severity levels: CRITICAL, HIGH, MEDIUM

### **Section 2: Severity Classification (around line 60)**
```python
if violation_type == 'full_admin':
    severity = 'CRITICAL'
elif violation_type == 'wildcard_actions':
    severity = 'HIGH'
```
- Classifies violations by severity
- Prioritizes remediation efforts

### **Section 3: Recommendations (around line 80)**
```python
recommendations = {
    'full_admin': 'Remove this policy immediately...',
    'wildcard_actions': 'Specify exact actions needed...'
}
```
- Provides actionable remediation steps
- Helps fix security issues

## 🎯 **Key Concept to Understand:**

**Severity Classification:**
- **CRITICAL**: Immediate action required (full admin access)
- **HIGH**: Fix within 24-48 hours (wildcard permissions)
- **MEDIUM**: Address within a week (overly broad permissions)

**Why Severity Matters:**
- Prioritizes remediation efforts
- Focuses on most dangerous issues first
- Efficient use of security team time
- Reduces overall risk faster

**Remediation Process:**
1. Identify violation type
2. Determine severity
3. Follow recommendation
4. Verify fix
5. Re-scan to confirm

## 💡 **Morning Practice Task:**

1. Open `least_privilege_checker.py`
2. Look at the 5 violation patterns
3. Read the severity classification logic
4. Answer this question: **Why is severity classification important for security teams?**

## 🚀 **Answer:**
Severity classification helps security teams prioritize remediation efforts by focusing on the most dangerous issues first. This reduces overall risk faster, makes efficient use of limited resources, and ensures critical vulnerabilities are addressed before they can be exploited.

---

**Time needed:** 15-20 minutes
**Difficulty:** Medium
**Skills:** Python, boto3, IAM, security analysis, severity classification, remediation
