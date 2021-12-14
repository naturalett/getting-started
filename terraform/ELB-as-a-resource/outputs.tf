# output "cluster_id" {
#   value = module.eks.cluster_id
# }

# https://registry.terraform.io/modules/terraform-aws-modules/elb/aws/latest/submodules/elb
output "elb_id" {
  value = aws_elb.ops.elb_id
#   value = concat(aws_elb.this.*.id, [""])[0]
}