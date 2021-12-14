# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/opsworks_stack
output "opsworks_id" {
    value = aws_opsworks_stack.main.id
}