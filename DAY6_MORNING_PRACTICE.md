# Day 6 Morning Practice - EBS Volume Remediator

## 🎯 **Practice Goal:**
Understand how to automatically clean up old, unattached EBS volumes to reduce costs and security risks.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `ebs-volume-remediator`
4. Click on: `ebs_remediator.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Get All Volumes (around line 20)**
```python
volumes = ec2.describe_volumes()['Volumes']
```
- Gets all EBS volumes in the account
- EBS = Elastic Block Store (virtual hard drives for EC2)

### **Section 2: Check if Attached (around line 30)**
```python
if len(volume['Attachments']) == 0:
```
- Checks if volume is attached to an EC2 instance
- If no attachments = unattached (orphaned volume)

### **Section 3: Check Age (around line 40)**
```python
days_old = (current_date - creation_date).days
if days_old > retention_days:
```
- Calculates how old the volume is
- If older than retention period (e.g., 30 days) = delete it

### **Section 4: Dry-Run Safety (around line 50)**
```python
if not dry_run:
    ec2.delete_volume(VolumeId=volume_id)
```
- Only deletes if dry_run = False
- Similar to S3 remediator - safety first!

## 🎯 **Key Concept to Understand:**

**What are EBS Volumes?**
- Virtual hard drives for EC2 instances
- Persist data even if EC2 instance is stopped
- Cost money even if not attached (orphaned volumes)

**What are Orphaned/Unattached Volumes?**
- Volumes not attached to any EC2 instance
- Can be leftover from deleted instances
- Still cost money every month
- Security risk (might contain sensitive data)

**Why Clean Them Up?**
- Cost savings (stop paying for unused storage)
- Security (remove potential data exposure)
- Clean environment (avoid clutter)

**Dry-Run Importance:**
- Test before deleting
- See what would be deleted
- Prevent accidental data loss

## 💡 **Morning Practice Task:**

1. Open `ebs_remediator.py`
2. Find the attachment check and age calculation
3. Read the deletion logic with dry-run
4. Answer this question: **Why is it important to clean up unattached EBS volumes?**

## 🚀 **Answer:**
Unattached EBS volumes still incur costs even though they're not being used. Cleaning them up reduces AWS bills, removes potential security risks from orphaned data, and keeps the environment clean and organized.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** Python, boto3, EC2, EBS volumes, cost optimization, data cleanup
