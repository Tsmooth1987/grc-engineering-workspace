variable "domain_name" {
  description = "Domain name for the website"
  type        = string
  default     = "terence-webster.com"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name_prefix" {
  description = "Prefix for S3 bucket name"
  type        = string
  default     = "terence-portfolio"
}
