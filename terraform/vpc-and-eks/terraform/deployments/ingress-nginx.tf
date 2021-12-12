locals {
  ingress_namespace = "ingress-nginx"
}

resource "helm_release" "ingress_nginx" {
  name       = "ingress-nginx"
  namespace  = kubernetes_namespace.namespaces[local.ingress_namespace].metadata[0].name
  repository = "https://kubernetes.github.io/ingress-nginx"
  chart      = "ingress-nginx"
  version    = "3.15.2"

  values = [<<EOF
  controller:
    service:
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: '*'
    config:
      use-http2: "true"
      use-proxy-protocol: "true"
  EOF
  ]

  set {
    name  = "controller.autoscaling.enabled"
    value = true
  }

  set {
    name  = "controller.autoscaling.minReplicas"
    value = 2
  }

  set {
    name  = "controller.autoscaling.targetCPUUtilizationPercentage"
    value = 80
  }
}

