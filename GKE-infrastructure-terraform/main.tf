resource "google_project_service" "enable_compute_api" {
  service = "compute.googleapis.com"
}
resource "google_project_service" "enable_container_api" {
  service = "container.googleapis.com"
}

resource "google_container_cluster" "primary" {
  name = var.cluster_name
  location = var.region

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 100
  }
  initial_node_count = 2
}

