resource "kubernetes_deployment" "my_app" {
  metadata {
    name      = "my-app"
    namespace = "default"
  }

  spec {
    replicas = 3

    selector {
      match_labels = {
        app = "my-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "my-app"
        }
      }

      spec {
        container {
          name  = "try-deployment"
          image = "azlanirshad/contact:1"

          port {
            container_port = 5000
          }
        }
      }
    }
  }
}
