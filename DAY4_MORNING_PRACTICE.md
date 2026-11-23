# Day 4 Morning Practice - GRC Alerter (SNS Email Notifications)

## 🎯 **Practice Goal:**
Understand how to send automated email alerts using AWS SNS when security issues are found.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `grc-alerter`
4. Click on: `iam_policy_alerter.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: SNS Client Setup (around line 15)**
```python
sns_client = boto3.client('sns')
```
- Creates connection to AWS SNS (Simple Notification Service)
- SNS is used for sending messages (email, SMS, etc.)

### **Section 2: SNS Topic (around line 20)**
```python
topic_arn = os.environ.get('SNS_TOPIC_ARN')
```
- Gets the SNS topic ARN (Amazon Resource Name)
- A topic is like a mailing list - people subscribe to it
- When you publish to the topic, all subscribers get the message

### **Section 3: Send Email Alert (around line 50)**
```python
sns_client.publish(
    TopicArn=topic_arn,
    Subject=f"Security Alert: {finding}",
    Message=message
)
```
- Publishes a message to the SNS topic
- Subject = email subject line
- Message = email body
- Subscribers receive it as email

## 🎯 **Key Concept to Understand:**

**What is AWS SNS?**
- Simple Notification Service
- Pub/Sub (Publish/Subscribe) messaging
- Used for sending alerts, notifications, messages
- Can send to email, SMS, mobile push, etc.

**How does email alerting work?**
1. Create an SNS topic
2. Subscribe your email to the topic
3. Your code publishes messages to the topic
4. SNS sends email to all subscribers

**Why is this useful for GRC?**
- Automatic notifications when security issues are found
- Immediate alerting for critical findings
- Don't have to manually check reports
- Can alert security team in real-time

## 💡 **Morning Practice Task:**

1. Open `iam_policy_alerter.py`
2. Find the SNS publish code
3. Read through the alert logic
4. Answer this question: **Why is automated email alerting important for security teams?**

## 🚀 **Answer:**
Automated email alerting enables security teams to respond quickly to security issues instead of waiting for manual report reviews. It provides real-time notifications when critical findings are detected, reducing response time and improving security posture.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** Python, boto3, SNS, email notifications, pub/sub messaging
