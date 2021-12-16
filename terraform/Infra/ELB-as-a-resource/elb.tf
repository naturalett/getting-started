# Create a new load balancer

# https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/string
resource "random_string" "random" {
  length           = 4
  special          = false
}

# https://registry.terraform.io/modules/terraform-aws-modules/elb/aws/latest
# https://registry.terraform.io/modules/terraform-aws-modules/elb/aws/latest/submodules/elb
# https://github.com/terraform-aws-modules/terraform-aws-elb/blob/master/modules/elb/main.tf
resource "aws_elb" "opsworks" {
  name               = "ElasticLB-${random_string.random.result}"
  subnets = ["subnet-5c892126", "subnet-4ca5c925"]

  # access_logs {
  #   bucket        = "opsworks"
  #   bucket_prefix = "docs"
  #   interval      = 60
  # }

  listener {
    instance_port     = 80
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }

  # listener {
  #   instance_port      = 8000
  #   instance_protocol  = "http"
  #   lb_port            = 443
  #   lb_protocol        = "https"
  #   ssl_certificate_id = "arn:aws:iam::123456789012:server-certificate/certName"
  # }

  health_check {
    healthy_threshold   = 3
    unhealthy_threshold = 2
    timeout             = 3
    target              = var.target_elb_healthcheck
    interval            = 10
  }

  # instances                   = [aws_instance.foo.id]
  cross_zone_load_balancing   = true
  idle_timeout                = 400
  connection_draining         = true
  connection_draining_timeout = 400

  tags = {
    Name = "ElasticLB"
  }
}