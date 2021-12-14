variable "cluster_name" {
  default = "echo-server-app"
}

variable "eks_version" {
  default = "1.18"
}

variable "instance_type" {
  description = "Instance type for the node group"
  default     = "t2.medium"
}

variable "region" {
  default = "eu-west-2"
}

variable "vpc_cidr" {
  default = "10.1.0.0/16"
}

variable "app_name" {
  default = "echo-server"
}

variable "app_version" {
  default = "v1.0.0"
}

variable "env_name" {
  description = "Will be used as tags for the node_groups and namespace on k8s"
  default     = "playground"
}
