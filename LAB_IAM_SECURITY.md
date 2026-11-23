# IAM Security Lab - Hands-On Practice

## 🎯 **Lab Objective:**
Create and manage IAM users with MFA, implement least-privilege policies, and audit IAM configurations.

## 📋 **Prerequisites:**
- AWS Console access
- Administrator permissions
- MFA device (virtual or hardware)

---

## 📖 **Step 1: Create IAM User**

**Step 1.1:** Go to AWS Console → IAM
**Step 1.2:** Click "Users" in left sidebar
**Step 1.3:** Click "Add users"
**Step 1.4:** Enter username: `grc-test-user`
**Step 1.5:** Select "AWS Management Console access"
**Step 1.6:** Click "Next: Permissions"
**Step 1.7:** Select "Attach existing policies directly"
**Step 1.8:** Search for and attach: `ReadOnlyAccess` (least privilege for testing)
**Step 1.9:** Click "Next: Tags"
**Step 1.10:** Add tag: `Purpose: Testing`
**Step 1.11:** Click "Next: Review"
**Step 1.12:** Click "Create user"
**Step 1.13:** **Important:** Copy the sign-in URL and temporary password
**Step 1.14:** Do NOT close this page yet

---

## 📖 **Step 2: Enable MFA on User**

**Step 2.1:** Still on the user creation page, click "Close"
**Step 2.2:** Find the user you just created: `grc-test-user`
**Step 2.3:** Click on the username
**Step 2.4:** Click "Security credentials" tab
**Step 2.5:** Click "Add MFA"
**Step 2.6:** Choose "Virtual MFA device"
**Step 2.7:** Follow the QR code setup with your authenticator app
**Step 2.8:** Enter two consecutive MFA codes
**Step 2.9:** Click "Assign MFA"

**Result:** User now has MFA enabled! ✅

---

## 📖 **Step 3: Create Custom Policy**

**Step 3.1:** Click "Policies" in left sidebar
**Step 3.2:** Click "Create policy"
**Step 3.3:** Click "JSON" tab
**Step 3.4:** Paste this policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::grc-test-bucket",
                "arn:aws:s3:::grc-test-bucket/*"
            ]
        }
    ]
}
```

**Step 3.5:** Click "Next: Tags"
**Step 3.6:** Click "Next: Review"
**Step 3.7:** Name: `S3-Limited-Access-Policy`
**Step 3.8:** Description: `Limited S3 access for testing`
**Step 3.9:** Click "Create policy"

**Result:** Custom policy created! ✅

---

## 📖 **Step 4: Attach Custom Policy to User**

**Step 4.1:** Go back to "Users"
**Step 4.2:** Click on `grc-test-user`
**Step 4.3:** Click "Add permissions"
**Step 4.4:** Click "Attach existing policies directly"
**Step 4.5:** Search for: `S3-Limited-Access-Policy`
**Step 4.6:** Check the box
**Step 4.7:** Click "Add permissions"

**Result:** User now has custom policy! ✅

---

## 📖 **Step 5: Test User Access**

**Step 5.1:** Use the sign-in URL from Step 1
**Step 5.2:** Log in as `grc-test-user`
**Step 5.3:** Enter MFA code when prompted
**Step 5.4:** Try to access S3 Console
**Step 5.5:** You should see buckets (ListAllMyBuckets)
**Step 5.6:** Try to access EC2 Console
**Step 5.7:** You should get "Access Denied" (least privilege working!)

**Result:** Least-privilege working! ✅

---

## 📖 **Step 6: Audit IAM Configuration**

**Step 6.1:** Log out of test user
**Step 6.2:** Log back in as administrator
**Step 6.3:** Go to IAM → "Access advisor"
**Step 6.4:** Click on `grc-test-user`
**Step 6.5:** Review last accessed services
**Step 6.6:** Review permissions in use
**Step 6.7:** Check if any services are unused

**Result:** Audit complete! ✅

---

## 📖 **Step 7: Clean Up**

**Step 7.1:** Go to IAM → Users
**Step 7.2:** Click on `grc-test-user`
**Step 7.3:** Click "Delete user"
**Step 7.4:** Confirm deletion
**Step 7.5:** Go to Policies
**Step 7.6:** Delete `S3-Limited-Access-Policy`

**Result:** Cleanup complete! ✅

---

## 🎯 **Lab Complete!**

**What You Learned:**
- ✅ Created IAM user with Console access
- ✅ Enabled MFA on user
- ✅ Created custom IAM policy
- ✅ Attached policy to user
- ✅ Tested least-privilege access
- ✅ Audited IAM configuration
- ✅ Cleaned up resources

**Skills Gained:**
- IAM user management
- MFA configuration
- Custom policy creation
- Least-privilege implementation
- Access testing
- IAM auditing

---

**Time needed:** 1-2 hours
**Difficulty:** Medium
**Skills:** IAM, MFA, policies, least-privilege, auditing
