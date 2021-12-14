# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/opsworks_stack
resource "aws_opsworks_stack" "main" {
  name                         = "awesome-stack"
  region                       = "us-east-1"
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