terraform {
  backend "s3" {
    bucket         = "thien-playground-tf-state-us-east-1"
    key            = "playground.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock"
  }
}