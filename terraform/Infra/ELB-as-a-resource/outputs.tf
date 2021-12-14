# https://registry.terraform.io/modules/terraform-aws-modules/elb/aws/latest/submodules/elb
output "elb_id" {
  value = concat(aws_elb.this.*.id, [""])[0]
}