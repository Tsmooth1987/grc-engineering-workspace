# EC2 Security Lab - Hands-On Practice

## 🎯 **Lab Objective:**
Launch EC2 instances, configure security groups, test SSH/RDP restrictions, and implement VPC security.

## 📋 **Prerequisites:**
- AWS Console access
- Administrator permissions
- SSH client (for Linux instances)
- AWS key pair (for SSH access)

---

## 📖 **Step 1: Create Security Group**

**Step 1.1:** Go to AWS Console → EC2

**Step 1.2:** Click "Security Groups" in the left sidebar

**Step 1.3:** Click "Create security group"

**Step 1.4:** Security group name: `grc-test-sg`

**Step 1.5:** Description: `Test security group for lab`

**Step 1.6:** VPC: Select your default VPC

**Step 1.7:** Inbound rules - Click "Add rule"

**Step 1.8:** Type: SSH, Source: My IP (or restrict to specific IP)

**Step 1.9:** Click "Create security group"

**Result:** Security group created! ✅

---

## 📖 **Step 2: Launch EC2 Instance**

**Step 2.1:** Click "Instances" in the left sidebar

**Step 2.2:** Click "Launch instances"

**Step 2.3:** Name: `grc-test-instance`

**Step 2.4:** AMI: Amazon Linux 2023 (free tier eligible)

**Step 2.5:** Instance type: t2.micro (free tier)

**Step 2.6:** Key pair: Create a new key pair or use existing

**Step 2.7:** Network settings: Select `grc-test-sg` security group

**Step 2.8:** Click "Launch instance"

**Result:** EC2 instance launching! ✅

---

## 📖 **Step 3: Review Security Group Rules**

**Step 3.1:** Go back to "Security Groups"

**Step 3.2:** Click on `grc-test-sg`

**Step 3.3:** Review inbound rules:
- SSH from your IP (safe)
- No HTTP/HTTPS from 0.0.0.0/0 (good)
- No RDP (good for Linux)

**Result:** Security group reviewed! ✅

---

## 📖 **Step 4: Test SSH Access**

**Step 4.1:** Wait for instance to be "Running"

**Step 4.2:** Get instance public IP

**Step 4.3:** Try SSH: `ssh -i your-key.pem ec2-user@public-ip`

**Step 4.4:** Should connect successfully

**Result:** SSH access working! ✅

---

## 📖 **Step 5: Test Access Restrictions**

**Step 5.1:** Modify security group to allow SSH from 0.0.0.0/0 (simulate mistake)

**Step 5.2:** Understand this is dangerous (anyone can connect)

**Step 5.3:** Revert back to your IP only

**Result:** Access restrictions tested! ✅

---

## 📖 **Step 6: Clean Up**

**Step 6.1:** Terminate EC2 instance

**Step 6.2:** Delete security group

**Step 6.3:** Delete key pair (optional)

**Result:** Cleanup complete! ✅

---

## 🎯 **Lab Complete!**

**What You Learned:**
- ✅ Created security group
- ✅ Launched EC2 instance
- ✅ Configured security group rules
- ✅ Tested SSH access
- ✅ Understood CIDR restrictions
- ✅ Tested access restrictions
- ✅ Cleaned up resources

**Skills Gained:**
- Security group configuration
- EC2 instance launch
- SSH access
- CIDR notation
- Access restrictions
- Security testing

---

**Time needed:** 1-2 hours
**Difficulty:** Medium
**Skills:** EC2, security groups, SSH, CIDR notation, network security
