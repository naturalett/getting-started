# VPC & EKS

## Prerequisits

- aws account configured with `aws configure`
- [jq](https://stedolan.github.io/jq/)

## Terraform

The terraform directory (which in every other case would be in a different
repository) creates our production resources.
To use:

First, we create the VPC and EKS modules:

```bash
cd terraform/
terraform init
terraform apply
```

### VPC

The module creates a dedicated VPC with 3 public and 3 private subnets, which
their CIDR is automatically generated based on `var.cidr`.

We specify only one NAT Gateway to be cost-efficient.

### EKS

Then, it procedes to create a managed EKS cluster with a single node group -
sized t2.medium (I think there should not be a cluster with smaller instance
type).

Creating the cluster takes about 15 minutes.
After the cluster has been created, we get the required data for `kubeconfig`
to actually do stuff on the cluster.

## See the service in production

First, we need to export our newly created kubeconfig:

```bash
export KUBECONFIG=terraform/kubeconfig_echo-server-app
```
