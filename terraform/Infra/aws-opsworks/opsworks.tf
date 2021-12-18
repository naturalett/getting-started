# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/opsworks_stack
resource "aws_opsworks_stack" "main" {
  depends_on = [aws_iam_role.test_role.id]
  name                         = "awesome-stack"
  region                       = var.region
  service_role_arn             = aws_iam_role.opsworks.arn
  default_instance_profile_arn = aws_iam_instance_profile.opsworks.arn

  tags = {
    Name = "foobar-terraform-stack"
  }

  custom_json = <<EOT
{
 "foobar": {
    "version": "1.0.0"
  }
}
EOT
}

resource "aws_iam_role" "test_role" {
  name = "test_role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })

  tags = {
    tag-key = "tag-value"
  }
}


resource "aws_iam_instance_profile" "test_profile" {
  depends_on = []
  name = "test_profile"
  role = aws_iam_role.role.name
}

resource "aws_iam_role" "role" {
  name = "test_role"
  path = "/"

  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
               "Service": "ec2.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
        }
    ]
}
EOF
}