variable "region" {
  default = "eu-west-2"
}

variable "target_elb_healthcheck" {
  default = "HTTP:8000/index.php"
}
