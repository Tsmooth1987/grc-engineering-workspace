# Day 20 Morning Practice - Terraform Networking Module

## 🎯 **Practice Goal:**
Review Terraform networking module to understand Infrastructure as Code for GRC.

## 📂 **Step 1: Open the Project**

1. Look at the file tree on the left
2. Find folder: `terraform/modules/networking`
3. Click on: `main.tf`

## 📖 **Step 2: Read the Code (10-15 minutes)**

Look for these key sections:

### **Section 1: VPC Resource (around line 10)**
```hcl
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support = true
  tags = var.tags
}
```
- Creates Virtual Private Cloud
- Defines network CIDR block
- Enables DNS features

### **Section 2: Subnets (around line 20)**
```hcl
resource "aws_subnet" "public" {
  vpc_id = aws_vpc.main.id
  cidr_block = var.public_subnet_cidr
  map_public_ip_on_launch = true
}
```
- Creates public subnet
- Allows public IP addresses
- Associates with VPC

### **Section 3: Security Groups (around line 40)**
```hcl
resource "aws_security_group" "web" {
  name = "${var.name}-web-sg"
  vpc_id = aws_vpc.main.id
  
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = var.allowed_cidr_blocks
  }
}
```
- Creates security group (firewall)
- Defines ingress rules
- Controls network access

## 🎯 **Key Concept to Understand:**

**Terraform vs CloudFormation:**
- Terraform: Multi-cloud, HCL language, popular with DevOps
- CloudFormation: AWS-native, YAML/JSON, tight AWS integration
- Both: Infrastructure as Code

**Networking Basics:**
- VPC: Virtual Private Cloud (isolated network)
- Subnets: Sub-networks within VPC
- Security Groups: Network-level firewalls
- NACLs: Network access control lists

**Why IaC for GRC:**
- Consistent security configurations
- Version control for infrastructure
- Compliance as code
- Automated compliance checks

## 💡 **Morning Practice Task:**

1. Open `main.tf` in terraform/modules/networking
2. Look at the VPC, subnet, and security group resources
3. Read through the HCL code
4. Answer this question: **Why is Infrastructure as Code important for GRC?**

## 🚀 **Answer:**
Infrastructure as Code enables consistent security configurations, version control for infrastructure, compliance as code with automated checks, and reproducible deployments. It ensures security controls are applied consistently and can be audited through code reviews.

---

**Time needed:** 10-15 minutes
**Difficulty:** Medium
**Skills:** Terraform, HCL, networking, VPC, subnets, security groups, IaC
