variable "region" {
  default = "eu-west-2"
}

variable "target_elb_healthcheck" {
  default = "HTTP:80/index.php"
}
