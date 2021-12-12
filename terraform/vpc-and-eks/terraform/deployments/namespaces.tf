resource "kubernetes_namespace" "namespaces" {
  for_each = toset([var.env_name, local.ingress_namespace])
  metadata {
    name = each.value
  }
}
