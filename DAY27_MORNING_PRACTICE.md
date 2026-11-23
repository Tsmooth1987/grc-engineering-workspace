# Day 27 Morning Practice - Terraform Basics Review

## 🎯 **Practice Goal:**
Review Terraform basics and understand Infrastructure as Code for GRC.

## 📂 **Step 1: Open Terraform Files**

1. Look at the file tree on the left
2. Find folder: `terraform/modules/networking`
3. Click on: `main.tf`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: Provider Block (around line 1)**
```hcl
provider "aws" {
  region = var.aws_region
}
```
- Defines AWS as cloud provider
- Sets region for resources
- Provider-specific configuration

### **Section 2: Resource Block (around line 10)**
```hcl
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  tags = var.tags
}
```
- Creates AWS resource
- Resource type: aws_vpc
- Resource name: main
- Uses variables for configuration

### **Section 3: Variables (around line 30)**
```hcl
variable "vpc_cidr" {
  type = string
  default = "10.0.0.0/16"
}
```
- Defines input variables
- Type checking
- Default values
- Reusable configuration

## 🎯 **Key Concept to Understand:**

**Terraform Core Concepts:**
- Provider: Cloud provider (AWS, Azure, GCP)
- Resource: Infrastructure component (VPC, EC2, S3)
- Variable: Input values for configuration
- Output: Values after infrastructure is created
- State: Tracks infrastructure state

**IaC Benefits for GRC:**
- Consistent security configurations
- Version control for infrastructure
- Compliance as code
- Reproducible deployments
- Audit trail through git history

**Terraform Workflow:**
1. Write code (HCL)
2. Initialize (terraform init)
3. Plan (terraform plan)
4. Apply (terraform apply)
5. Destroy (terraform destroy)

## 💡 **Morning Practice Task:**

1. Open `main.tf` in terraform/modules/networking
2. Read through the HCL code
3. Understand the resource blocks
4. Answer this question: **Why is Terraform better than the AWS Console for GRC engineering?**

## 🚀 **Answer:**
Terraform provides Infrastructure as Code, which means security configurations are version-controlled, reproducible, and can be reviewed through code reviews. The Console is manual and error-prone, while Terraform ensures consistent, auditable deployments that can be tested before applying.

---

**Time needed:** 10-15 minutes
**Difficulty:** Medium
**Skills:** Terraform, HCL, IaC, version control, AWS infrastructure
