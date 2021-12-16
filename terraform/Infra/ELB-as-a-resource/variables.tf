variable "region" {
  default = "us-east-1"
}

variable "target_elb_healthcheck" {
  default = "HTTP:8000/index.php"
}
