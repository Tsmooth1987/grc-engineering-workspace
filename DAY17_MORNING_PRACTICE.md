# Day 17 Morning Practice - AI Risk Assessment Tool Review

## 🎯 **Practice Goal:**
Review the AI Risk Assessment Tool to understand ISO/IEC 42001 compliance and AI governance.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `ai-risk-assessment-tool`
4. Click on: `main.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: AI System Classification (around line 50)**
```python
classification = self.classifier.classify_system(
    system_description,
    system_features
)
```
- Classifies AI system type
- Determines if it's Generative AI or not
- Critical for compliance requirements

### **Section 2: Risk Scoring (around line 60)**
```python
risk_score = self.risk_engine.calculate_risk_score(
    impact, likelihood, vulnerability
)
```
- Calculates risk score based on factors
- Higher score = higher risk
- Used for prioritization

### **Section 3: ISO/IEC 42001 Controls (around line 70)**
```python
required_controls = self._get_controls_for_categories(
    required_control_categories
)
```
- Maps to ISO/IEC 42001 controls
- AI Management System standard
- Required controls based on risk level

## 🎯 **Key Concept to Understand:**

**ISO/IEC 42001:**
- International standard for AI Management Systems
- Like ISO 27001 but for AI systems
- Ensures responsible AI development and deployment

**AI Governance Importance:**
- Prevents bias and discrimination
- Ensures privacy and data protection
- Regulatory compliance requirements
- Builds trust with stakeholders

**Risk Factors:**
- Impact: How bad if it fails
- Likelihood: Probability of failure
- Vulnerability: Security weaknesses

## 💡 **Morning Practice Task:**

1. Open `main.py` in ai-risk-assessment-tool
2. Look at the AI system classification
3. Read the risk scoring logic
4. Answer this question: **Why is AI governance important for organizations?**

## 🚀 **Answer:**
AI governance ensures AI systems are developed and deployed responsibly, addressing risks like bias, privacy issues, and unintended consequences. It ensures compliance with regulations, builds trust with stakeholders, and mitigates potential harm from AI systems.

---

**Time needed:** 10-15 minutes
**Difficulty:** Medium
**Skills:** Python, AI governance, ISO/IEC 42001, risk assessment, compliance
