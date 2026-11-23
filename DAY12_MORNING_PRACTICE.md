# Day 12 Morning Practice - Enable AWS Config Managed Rule

## 🎯 **Practice Goal:**
Enable a managed AWS Config rule in your account to start monitoring configurations.

## 📂 **Step 1: Go to AWS Console**

1. Open browser
2. Go to: console.aws.amazon.com
3. Navigate to AWS Config service

## 📂 **Step 2: Enable a Managed Rule**

1. Click "Rules" in left sidebar
2. Click "Add rule"
3. Choose "AWS managed rules"
4. Find: "s3-bucket-server-side-encryption-enabled" (S3 encryption check)
5. Click "Next"
6. Configure parameters (keep defaults)
7. Click "Next" again
8. Review and click "Add rule"

## 🎯 **What This Does:**

This rule checks if all your S3 buckets have server-side encryption enabled.

**COMPLIANT:** Encryption enabled
**NON-COMPLIANT:** Encryption not enabled

## 💡 **Morning Practice Task:**

1. Enable the S3 encryption rule
2. Check compliance status after enabling
3. Answer this question: **Why is server-side encryption important for S3 buckets?**

## 🚀 **Answer:**
Server-side encryption protects data at rest in S3 buckets by encrypting objects before storage and decrypting on retrieval. This ensures data confidentiality and compliance with security best practices and regulatory requirements.

---

**Time needed:** 10 minutes
**Difficulty:** Easy
**Skills:** AWS Console, Config managed rules, S3 encryption
