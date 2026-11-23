# Day 26 Morning Practice - GuardDuty Introduction

## 🎯 **Practice Goal:**
Understand GuardDuty basics and threat detection for AWS environments.

## 📂 **Step 1: Learn About GuardDuty**

**What is GuardDuty?**
- AWS threat detection service
- Uses machine learning and anomaly detection
- Analyzes AWS CloudTrail events, VPC Flow Logs, DNS logs
- Detects compromised instances, reconnaissance, crypto mining

**Key Features:**
- 30-day free trial, then $1/region/million events
- Continuous monitoring
- Integration with Security Hub
- Automated remediation via Lambda

## 📖 **Step 2: Common Finding Types**

**Infrastructure:**
- CryptoCurrency: Mining operations
- Trojan: Malware indicators
- Reconnaissance: Pre-attack behavior

**Authentication:**
- UnauthorizedAccess: Suspicious access patterns
- IAMUser: Compromised credentials
- MFA: Disabled MFA on critical accounts

**Network:**
- Backdoor: Remote access tools
- DNS: Suspicious DNS requests
- PortScanning: Network reconnaissance

## 🎯 **Key Concept to Understand:**

**Threat Detection vs. Prevention:**
- Prevention: Security groups, IAM policies (block attacks)
- Detection: GuardDuty, CloudTrail (find attacks that happen)
- Response: Automated remediation (stop attacks)

**Why GuardDuty Matters:**
- Finds threats you can't prevent
- Real-time alerting
- Reduces detection time
- Integrates with existing security tools

## 💡 **Morning Practice Task:**

1. Review the GUARDDUTY_INTEGRATION_GUIDE.md file
2. Understand the finding types
3. Read the remediation patterns
4. Answer this question: **Why is threat detection important in addition to prevention?**

## 🚀 **Answer:**
Threat detection is important because prevention alone can't stop all attacks. Even with strong security controls, attackers can find ways in. Detection helps you find active threats quickly, reduce dwell time, and respond before significant damage occurs.

---

**Time needed:** 10-15 minutes
**Difficulty:** Easy
**Skills:** GuardDuty, threat detection, security monitoring, incident response
