# Day 7 Morning Practice - AI Risk Assessment Tool

## 🎯 **Practice Goal:**
Understand AI governance and ISO/IEC 42001 compliance for AI systems.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `ai-risk-assessment-tool`
4. Click on: `main.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: AI System Classification (around line 30)**
```python
def classify_ai_system(system_type, purpose, autonomy_level)
```
- Classifies what type of AI system it is
- Determines if it's Generative AI or not
- Critical for compliance requirements

### **Section 2: Risk Scoring (around line 50)**
```python
def calculate_risk_score(impact, likelihood, vulnerability)
```
- Calculates risk score based on factors
- Higher score = higher risk
- Used for prioritization

### **Section 3: ISO/IEC 42001 Controls (around line 70)**
```python
def get_iso_42001_controls(ai_type, risk_level)
```
- Maps to ISO/IEC 42001 controls
- AI Management System standard
- Required controls based on risk level

## 🎯 **Key Concept to Understand:**

**What is ISO/IEC 42001?**
- International standard for AI Management Systems
- Like ISO 27001 but for AI systems
- Ensures responsible AI development and deployment

**Why AI Governance is Important:**
- AI systems can have unintended consequences
- Bias, discrimination, privacy issues
- Regulatory compliance requirements
- Trust and transparency

**Risk Factors for AI:**
- Impact (how bad if it fails)
- Likelihood (probability of failure)
- Vulnerability (security weaknesses)

## 💡 **Morning Practice Task:**

1. Open `main.py` in ai-risk-assessment-tool
2. Look at the AI system classification logic
3. Read the risk scoring calculation
4. Answer this question: **Why is AI governance important for organizations?**

## 🚀 **Answer:**
AI governance ensures AI systems are developed and deployed responsibly, addressing risks like bias, privacy issues, and unintended consequences. It ensures compliance with regulations, builds trust with stakeholders, and mitigates potential harm from AI systems.

---

**Time needed:** 10-15 minutes
**Difficulty:** Medium
**Skills:** Python, AI governance, ISO/IEC 42001, risk assessment, compliance
