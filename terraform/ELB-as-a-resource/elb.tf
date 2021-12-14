# Create a new load balancer

# https://registry.terraform.io/modules/terraform-aws-modules/elb/aws/latest
# https://registry.terraform.io/modules/terraform-aws-modules/elb/aws/latest/submodules/elb
# https://github.com/terraform-aws-modules/terraform-aws-elb/blob/master/modules/elb/main.tf
resource "aws_elb" "ops" {
  name               = "ElasticLB"
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

  access_logs {
    bucket        = "ops"
    bucket_prefix = "ops2"
    interval      = 60
  }

  listener {
    instance_port     = 8000
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
    target              = "HTTP:8000/index.php"
    interval            = 10
  }

  instances                   = [aws_instance.foo.id]
  cross_zone_load_balancing   = true
  idle_timeout                = 400
  connection_draining         = true
  connection_draining_timeout = 400

  tags = {
    Name = "ElasticLB"
  }
}