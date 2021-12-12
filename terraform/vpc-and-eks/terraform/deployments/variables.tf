variable "cluster_id" {
}

variable "region" {
  default = "eu-west-1"
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
