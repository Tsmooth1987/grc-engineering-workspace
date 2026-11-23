# Day 9 Morning Practice - Security Hub Custom Controls

## 🎯 **Practice Goal:**
Understand how to create custom Security Hub controls beyond standard FSBP/CIS benchmarks for specific business requirements.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `grc-security-hub-custom-controls`
4. Click on: `custom_controls/custom_compliance_control.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Custom Control Definition (around line 20)**
```python
class CustomComplianceControl:
    def __init__(self, control_id, control_name, description):
```
- Defines a custom Security Hub control
- Unique control ID and name
- Description of what it checks

### **Section 2: Compliance Check Logic (around line 40)**
```python
def evaluate_compliance(self, resource_config):
    # Custom logic to check if resource is compliant
    return True/False, finding_details
```
- Your custom compliance logic
- Returns compliance status
- Provides details about any violations

### **Section 3: Security Hub Integration (around line 60)**
```python
securityhub.batch_import_findings(Findings=[findings])
```
- Imports findings into Security Hub
- Makes them visible in Security Hub console
- Enables tracking and reporting

## 🎯 **Key Concept to Understand:**

**What are Custom Security Hub Controls?**
- Beyond standard benchmarks (FSBP, CIS)
- Tailored to your specific business requirements
- Custom compliance rules for your environment

**Why Custom Controls?**
- Standard benchmarks don't cover all scenarios
- Industry-specific requirements
- Company-specific security policies
- Regulatory compliance needs

**How They Work:**
1. Define control logic
2. Check resources for compliance
3. Import findings into Security Hub
4. Track and report like standard findings

## 💡 **Morning Practice Task:**

1. Open `custom_compliance_control.py`
2. Look at the custom control class structure
3. Read the compliance evaluation logic
4. Answer this question: **Why would an organization need custom Security Hub controls beyond standard benchmarks?**

## 🚀 **Answer:**
Organizations need custom controls to address industry-specific requirements, company-specific security policies, and regulatory compliance needs that standard benchmarks (FSBP, CIS) don't cover. Custom controls provide tailored security monitoring for unique business scenarios.

---

**Time needed:** 10-15 minutes
**Difficulty:** Medium
**Skills:** Python, Security Hub custom controls, compliance logic, benchmark customization
