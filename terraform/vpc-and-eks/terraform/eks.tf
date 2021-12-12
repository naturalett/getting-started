# https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "13.2.1"

  cluster_name                    = var.cluster_name
  cluster_version                 = var.eks_version
  subnets                         = module.vpc.private_subnets
  vpc_id                          = module.vpc.vpc_id
  cluster_endpoint_private_access = true
  # cluster_endpoint_public_access                 = true
  # cluster_endpoint_public_access_cidrs = ["${chomp(data.http.local_ip.body)}/32"]
  # cluster_create_endpoint_private_access_sg_rule = true

  node_groups = {
    "nodes" = {
      desired_capacity = 1
      max_capacity     = 2
      min_capacity     = 1
      key_name         = "echo-server"

      instance_type = var.instance_type
      k8s_labels = {
        instancegroup = "nodes"
        Environment   = var.env_name
      }
      additional_tags = {
        Name = "nodes.${var.cluster_name}"
      }
    }
  }
}
