variable "instance_type" {
  description = "Instance type for the node group"
  default     = "t2.medium"
}

variable "region" {
  default = "us-east-1"
}

variable "stack_id" {
  default = "ops-works"
}
