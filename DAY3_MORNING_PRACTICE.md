# Day 3 Morning Practice - EC2 Security Auditor

## 🎯 **Practice Goal:**
Understand how to audit EC2 security groups for risky configurations like SSH open to the world.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `ec2-security-auditor`
4. Click on: `ec2_security_auditor.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Main Connection (around line 15)**
```python
ec2_client = boto3.client('ec2')
```
- Connects to AWS EC2 service
- Like opening a connection to your EC2 instances

### **Section 2: Get Security Groups (around line 20)**
```python
response = ec2_client.describe_security_groups()
```
- Gets all security groups in your account
- Security groups are like firewalls for EC2 instances

### **Section 3: The Risk Check (around line 40)**
```python
for rule in security_group['IpPermissions']:
    if rule.get('IpProtocol') == 'tcp':
        for ip_range in rule.get('IpRanges', []):
            if ip_range.get('CidrIp') == '0.0.0.0/0':
                if rule.get('FromPort') == 22:
```

**This is checking for:**
- TCP protocol
- IP range `0.0.0.0/0` (which means "anyone in the world")
- Port 22 (which is SSH)

**This = SSH open to the entire world = VERY DANGEROUS!**

## 🎯 **Key Concept to Understand:**

**What is a Security Group?**
- Like a firewall for EC2 instances
- Controls what traffic can go in and out
- Rules allow or block traffic

**What is SSH (Port 22)?**
- SSH = Secure Shell
- Used to remotely connect to servers
- Port 22 is the standard SSH port

**What is `0.0.0.0/0`?**
- CIDR notation for "any IP address"
- Means "anyone on the internet"
- Like leaving your front door unlocked for the whole world

**Why is SSH open to 0.0.0.0/0 dangerous?**
- Anyone on the internet can try to connect
- Brute force attacks (hackers trying passwords)
- Potential unauthorized access
- If they get in, they can control your server

## 💡 **Morning Practice Task:**

1. Open `ec2_security_auditor.py`
2. Find the code that checks for SSH open to 0.0.0.0/0
3. Read through the logic
4. Answer this question: **Why is it bad to have SSH (port 22) open to 0.0.0.0/0?**

## 🚀 **Answer:**
SSH open to 0.0.0.0/0 means anyone on the internet can try to connect to your server. This exposes you to brute force attacks, unauthorized access attempts, and potential server compromise. It's like leaving your front door unlocked for the entire world.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** Python, boto3, EC2, security groups, CIDR notation
