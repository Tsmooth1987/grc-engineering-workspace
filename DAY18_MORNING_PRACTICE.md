# Day 18 Morning Practice - Security Hub Custom Controls Deep Dive

## 🎯 **Practice Goal:**
Deep dive into Security Hub Custom Controls to understand custom compliance logic beyond standard benchmarks.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `GRC-PROJECTS`
3. Click on: `grc-security-hub-custom-controls`
4. Click on: `custom_controls/custom_compliance_control.py`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Control Initialization (around line 20)**
```python
def __init__(self, event: Dict[str, Any]):
    self.event = event
    self.security_hub = boto3.client('securityhub')
```
- Initializes the custom control
- Sets up AWS clients
- Prepares for evaluation

### **Section 2: Compliance Evaluation (around line 40)**
```python
def evaluate_compliance(self, resource_config):
    # Custom logic to check if resource is compliant
    return compliance_status, finding_details
```
- Your custom compliance logic
- Returns COMPLIANT or NON_COMPLIANT
- Provides detailed findings

### **Section 3: Finding Import (around line 60)**
```python
securityhub.batch_import_findings(Findings=[findings])
```
- Imports findings into Security Hub
- Makes them visible in console
- Enables tracking and reporting

## 🎯 **Key Concept to Understand:**

**Why Custom Controls?**
- Standard benchmarks (FSBP, CIS) are general-purpose
- Industry-specific requirements
- Company-specific security policies
- Regulatory compliance needs

**Control Logic:**
- Input: AWS resource configuration
- Processing: Custom compliance check
- Output: COMPLIANT/NON_COMPLIANT with details

**Finding Import:**
- Makes findings visible in Security Hub
- Enables centralized tracking
- Integrates with existing workflows

## 💡 **Morning Practice Task:**

1. Open `custom_compliance_control.py`
2. Look at the control initialization
3. Read the compliance evaluation logic
4. Answer this question: **Why would an organization need custom Security Hub controls beyond standard benchmarks?**

## 🚀 **Answer:**
Organizations need custom controls to address industry-specific requirements, company-specific security policies, and regulatory compliance needs that standard benchmarks (FSBP, CIS) don't cover. Custom controls provide tailored security monitoring for unique business scenarios.

---

**Time needed:** 10-15 minutes
**Difficulty:** Medium
**Skills:** Python, Security Hub custom controls, compliance logic, benchmark customization
