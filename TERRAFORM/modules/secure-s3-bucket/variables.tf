variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "tags" {
  description = "A map of tags to add to all resources"
  type        = map(string)
  default = {
    Environment = "dev"
    Owner       = "terence-webster"
  }
}

# Add this new variable
variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
  default     = "pci-monitoring-bucket"  
}
