resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "project-talia"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "job_status"
  range_key      = "job_id"

  attribute {
    name = "job_status"
    type = "S"
  }

  attribute {
    name = "job_id"
    type = "N"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = true
  }

  tags = {
    Name        = "dynamodb-table-1"
    Environment = "production"
  }
}