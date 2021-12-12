resource "kubernetes_config_map" "index_html" {
  metadata {
    name      = "index.html"
    namespace = kubernetes_namespace.namespaces[var.env_name].metadata[0].name
  }
  data = {
    "index.html" = file("${path.module}/../../index.html")
  }
}

resource "helm_release" "echo_server" {
  name      = "echo-server"
  namespace = kubernetes_namespace.namespaces[var.env_name].metadata[0].name
  chart     = "${path.module}/../../kubernetes/"

  values = [<<EOF
volumes:
  - configMap:
      name: ${kubernetes_config_map.index_html.metadata[0].name}
    name: index-html
volumeMounts:
  - mountPath: /static
    name: index-html
env:
  - name: INDEX_PATH
    value: /static
  EOF
  ]

  set {
    name  = "nameOverride"
    value = var.app_name
  }

  set {
    name  = "fullnameOverride"
    value = var.app_name
  }

  set {
    name  = "image.tag"
    value = var.app_version
  }

}
