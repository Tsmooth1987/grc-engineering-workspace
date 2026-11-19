# 1. Provider Configuration
provider "aws" {
  region = "us-east-1"
}

# 2. Variables
variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

# 3. Networking Module
module "networking" {
  source = "./modules/networking"

  vpc_cidr            = "10.0.0.0/16"
  environment         = "dev"
  public_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs = ["10.0.101.0/24", "10.0.102.0/24"]
  availability_zones  = ["us-east-1a", "us-east-1b"]
  tags = {
    Environment = "dev"
    Project     = "pci-monitoring"
    ManagedBy   = "terraform"
  }
}

# 4. S3 Bucket Module
module "secure_bucket" {
  source = "./modules/secure-s3-bucket"
  bucket_name = "pci-monitoring-${var.environment}"
  environment = "dev"
  tags = {
    Environment = "dev"
    Project     = "pci-monitoring"
    ManagedBy   = "terraform"
  }
}