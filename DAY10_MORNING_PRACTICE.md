# Day 10 Morning Practice - AWS Config Introduction

## 🎯 **Practice Goal:**
Understand AWS Config basics and how it complements Security Hub for compliance monitoring.

## 📖 **What is AWS Config?**

**AWS Config** is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources.

**Key Concepts:**
- **Config Rules:** Automated checks against best practices
- **Periodic Rules:** Run on a schedule (e.g., every 24 hours)
- **Trigger-Based Rules:** Run when resources change
- **Managed Rules:** Pre-built rules by AWS
- **Custom Rules:** Your own custom logic

**How it differs from Security Hub:**
- **Security Hub:** Aggregates findings from multiple services (including Config)
- **Config:** Deep configuration monitoring for specific services
- **Together:** Config feeds findings to Security Hub for centralized view

## 🎯 **Practice Task (No Code Required):**

**1. Go to AWS Console** (console.aws.amazon.com)
**2. Navigate to AWS Config**
**3. Look at existing rules** (if any enabled)
**4. Review managed rules** available
**5. Answer this question:**

**What is the difference between Security Hub and AWS Config?**

**A)** They are the same thing  
**B)** Security Hub aggregates findings, Config monitors configurations  
**C)** Config is for monitoring, Security Hub is for alerts  
**D)** Config is free, Security Hub costs money

## 🚀 **Answer:**
Security Hub aggregates security findings from multiple AWS services (including Config) into a centralized view, while AWS Config specifically monitors and evaluates the configurations of AWS resources. Config feeds its findings to Security Hub, and together they provide comprehensive compliance monitoring.

---

**Time needed:** 10 minutes (console exploration)
**Difficulty:** Easy
**Skills:** AWS Config, console navigation, rule concepts
