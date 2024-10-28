resource "kubernetes_service" "my_app_service" {
  metadata {
    name = "terraform-deploy-service"
  }

  spec {
    selector = {
      app = kubernetes_deployment.my_app.spec[0].template[0].metadata[0].labels["app"]
    }

    type = "LoadBalancer"

    port {
      port        = 80
      target_port = 5000
    }
  }
}
