# S3 Security Lab - Hands-On Practice

## 🎯 **Lab Objective:**
Create S3 buckets with different security settings, implement bucket policies, test public access blocking, enable encryption and versioning.

## 📋 **Prerequisites:**
- AWS Console access
- Administrator permissions

---

## 📖 **Step 1: Create S3 Bucket**

**Step 1.1:** Go to AWS Console → S3

**Step 1.2:** Click "Create bucket"

**Step 1.3:** Bucket name: `grc-test-bucket-unique` (must be globally unique)

**Step 1.4:** Region: US East (N. Virginia) us-east-1

**Step 1.5:** Uncheck "Block all public access" (we'll test this later)

**Step 1.6:** Click "Create bucket"

**Result:** S3 bucket created! ✅

---

## 📖 **Step 2: Enable Bucket Encryption**

**Step 2.1:** Click on the bucket name: `grc-test-bucket-unique`

**Step 2.2:** Click "Properties" tab

**Step 2.3:** Scroll down to "Default encryption"

**Step 2.4:** Click "Edit"

**Step 2.5:** Select "Enable"

**Step 2.6:** Encryption type: SSE-S3 (AWS-managed keys)

**Step 2.7:** Bucket key: Disabled

**Step 2.8:** Click "Save changes"

**Result:** Encryption enabled! ✅

---

## 📖 **Step 3: Enable Versioning**

**Step 3.1:** Still in bucket properties, scroll to "Bucket Versioning"

**Step 3.2:** Click "Edit"

**Step 3.3:** Select "Enable"

**Step 3.4:** Click "Save changes"

**Result:** Versioning enabled! ✅

---

## 📖 **Step 4: Implement Bucket Policy**

**Step 4.1:** Click "Permissions" tab

**Step 4.2:** Scroll to "Bucket policy"

**Step 4.3:** Click "Edit"

**Step 4.4:** Paste this policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::grc-test-bucket-unique",
                "arn:aws:s3:::grc-test-bucket-unique/*"
            ],
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}
```

**Step 4.5:** This policy denies all access unless using HTTPS

**Step 4.6:** Click "Save changes"

**Result:** HTTPS-only policy enabled! ✅

---

## 📖 **Step 5: Test Public Access Blocking**

**Step 5.1:** Click "Permissions" tab

**Step 5.2:** Scroll to "Block public access (bucket settings)"

**Step 5.3:** Click "Edit"

**Step 5.4:** Enable "Block public access to bucket and objects granted through new public bucket policies"

**Step 5.5:** Enable "Block public access to bucket and objects granted through any public bucket policies"

**Step 5.6:** Click "Save changes"

**Result:** Public access blocked! ✅

---

## 📖 **Step 6: Upload Test File**

**Step 6.1:** Click "Objects" tab

**Step 6.2:** Click "Upload"

**Step 6.3:** Drag and drop a test file (any small file)

**Step 6.4:** Click "Upload"

**Result:** Test file uploaded! ✅

---

## 📖 **Step 7: Test Security Settings**

**Step 7.1:** Try to access the file via HTTP (should be denied by our policy)

**Step 7.2:** Check the file properties - should show encryption

**Step 7.3:** Upload the same file again - should create a new version

**Result:** Security controls verified! ✅

---

## 📖 **Step 8: Clean Up**

**Step 8.1:** Delete all objects in the bucket

**Step 8.2:** Delete the bucket

**Step 8.3:** Confirm deletion

**Result:** Cleanup complete! ✅

---

## 🎯 **Lab Complete!**

**What You Learned:**
- ✅ Created S3 bucket
- ✅ Enabled encryption (SSE-S3)
- ✅ Enabled versioning
- ✅ Implemented HTTPS-only bucket policy
- ✅ Blocked public access
- ✅ Uploaded test file
- ✅ Verified security controls
- ✅ Cleaned up resources

**Skills Gained:**
- S3 bucket creation
- Encryption configuration
- Versioning configuration
- Bucket policy implementation
- Public access blocking
- Security testing

---

**Time needed:** 1-2 hours
**Difficulty:** Medium
**Skills:** S3, encryption, versioning, bucket policies, public access blocking
