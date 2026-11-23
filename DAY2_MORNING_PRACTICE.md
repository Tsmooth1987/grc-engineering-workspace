# Day 2 Morning Practice - S3 Auto-Remediator

## 🎯 **Practice Goal:**
Understand how to automatically fix security issues in AWS S3 buckets.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `s3-auto-remediator`
4. Click on: `s3_remediator.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Main Function (around line 20)**
```python
def lambda_handler(event, context):
```
- This is the main function that runs

### **Section 2: The Safety Check (around line 25)**
```python
dry_run = event.get('dry_run', True)
```
- This is a **safety feature**
- `dry_run = True` means "don't actually change anything, just tell me what you would do"
- Like a "test mode" - safe to practice

### **Section 3: Check S3 Buckets (around line 35)**
```python
for bucket in s3.list_buckets()['Buckets']:
```
- Goes through each S3 bucket
- Checks if versioning is enabled
- Checks if public access is blocked

### **Section 4: The Fix (around line 50)**
```python
if not dry_run:
    s3.put_bucket_versioning(...)
```
- Only runs if `dry_run = False`
- Actually enables versioning on the bucket
- This is the "remediation" part

## 🎯 **Key Concept to Understand:**

**What is "Auto-Remediation"?**
- Automatically fixing security issues
- Instead of just reporting the problem
- The code actually fixes it
- Like a self-healing system

**Why the `--dry-run` flag is important:**
- Lets you test without making changes
- See what would happen before it happens
- Prevents accidental changes
- Safety first!

## 💡 **Morning Practice Task:**

1. Open `s3_remediator.py`
2. Find the `dry_run` check
3. Read through the code
4. Answer this question: **Why is the `dry_run` feature important for security automation?**

## 🚀 **Answer:**
The `dry_run` feature lets you test the automation safely without actually making changes. This prevents accidental modifications and lets you verify the logic before running it for real.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** Python, boto3, S3, safety features
