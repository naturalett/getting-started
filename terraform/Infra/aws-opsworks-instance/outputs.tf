# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/opsworks_instance
output "aws_opsworks_instance_id" {
  value = aws_opsworks_instance.instance.id
}