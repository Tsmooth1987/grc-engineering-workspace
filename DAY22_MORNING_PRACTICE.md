# Day 22 Morning Practice - GRC Alerter (SNS) Deep Dive

## 🎯 **Practice Goal:**
Deep dive into GRC Alerter to understand SNS email notifications and automated alerting.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `grc-alerter`
4. Click on: `iam_policy_alerter.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: SNS Client Setup (around line 20)**
```python
sns_client = boto3.client('sns')
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:291846646255:GRC-Alerts"
```
- Creates SNS client
- Defines SNS topic ARN
- Topic acts as a mailing list

### **Section 2: Findings Detection (around line 40)**
```python
is_admin_access = (
    statement.get('Effect') == 'Allow' and
    statement.get('Action') == '*' and
    statement.get('Resource') == '*'
)
```
- Detects admin access policies
- High-risk pattern identification

### **Section 3: Send SNS Alert (around line 80)**
```python
sns_client.publish(
    TopicArn=SNS_TOPIC_ARN,
    Subject=subject,
    Message=message
)
```
- Publishes message to SNS topic
- Triggers email to subscribers
- Real-time notification

## 🎯 **Key Concept to Understand:**

**SNS (Simple Notification Service):**
- Pub/Sub messaging service
- Can send to email, SMS, mobile push
- Topic-based routing

**Pub/Sub Pattern:**
- Publishers send messages to topics
- Subscribers receive from topics
- Decoupled architecture

**Email Alerting Benefits:**
- Real-time security notifications
- Immediate response to threats
- No need to check reports manually
- Can alert on-call teams

## 💡 **Morning Practice Task:**

1. Open `iam_policy_alerter.py`
2. Look at the SNS publish code
3. Read the alert logic
4. Answer this question: **Why is automated email alerting important for security teams?**

## 🚀 **Answer:**
Automated email alerting enables security teams to respond quickly to security issues instead of waiting for manual report reviews. It provides real-time notifications when critical findings are detected, reducing response time and improving security posture.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** Python, boto3, SNS, email notifications, pub/sub messaging
