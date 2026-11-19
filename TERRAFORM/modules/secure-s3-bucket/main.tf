resource "aws_s3_bucket" "secure_bucket" {
  bucket = var.bucket_name
  acl    = "private"
  
  tags = merge(
    var.tags,
    {
      Name = var.bucket_name
    }
  )
}

# Rest of your configuration remains the same...

resource "aws_s3_bucket_public_access_block" "block_public_access" {
  bucket = aws_s3_bucket.secure_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
  bucket = aws_s3_bucket.secure_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }

  depends_on = [aws_s3_bucket.secure_bucket]
}
