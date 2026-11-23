# Day 21 Morning Practice - EC2 Security Group Auditor Deep Dive

## 🎯 **Practice Goal:**
Deep dive into EC2 Security Group Auditor to understand network security controls.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `ec2-security-auditor`
4. Click on: `ec2_security_auditor.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Get Security Groups (around line 20)**
```python
response = ec2_client.describe_security_groups()
security_groups = response['SecurityGroups']
```
- Gets all security groups in the account
- Lists SG rules and configurations

### **Section 2: Check for SSH/RDP Open to World (around line 50)**
```python
if ip_range.get('CidrIp') == '0.0.0.0/0':
    if from_port <= 22 <= to_port:
        # SSH open to world
```
- Checks for SSH (port 22) open to 0.0.0.0/0
- Checks for RDP (port 3389) open to 0.0.0.0/0
- Critical security risk

### **Section 3: Report Findings (around line 70)**
```python
audit_findings.append({
    'GroupID': group_id,
    'GroupName': group_name,
    'RiskyRule': description
})
```
- Records risky rules
- Generates compliance report
- Enables remediation

## 🎯 **Key Concept to Understand:**

**Security Groups:**
- Network-level firewalls for EC2
- Stateful: allows return traffic automatically
- Rules evaluated in order (allow/deny)

**CIDR Notation:**
- 0.0.0.0/0 = Any IP address (entire internet)
- 10.0.0.0/8 = Specific IP range
- 192.168.1.1/32 = Single IP

**SSH/RDP Risks:**
- SSH (22): Remote access to Linux servers
- RDP (3389): Remote access to Windows servers
- Open to world = Brute force attacks, unauthorized access

## 💡 **Morning Practice Task:**

1. Open `ec2_security_auditor.py`
2. Look at the SSH/RDP check logic
3. Read the CIDR notation
4. Answer this question: **Why is SSH open to 0.0.0.0/0 dangerous?**

## 🚀 **Answer:**
SSH open to 0.0.0.0/0 means anyone on the internet can attempt to connect to your server. This exposes you to brute force attacks, unauthorized access attempts, and potential server compromise if credentials are guessed or stolen.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** Python, boto3, EC2, security groups, CIDR notation, network security
