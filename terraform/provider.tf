provider "google" {
  project = "gcp-deployment-439420"
  region  = "us-central1-c"
}

data "google_container_cluster" "primary" {
  name     = "gke-cluster"
  location = "us-central1-c"
}


provider "kubernetes" {
  host                   = "https://34.56.179.251"
  token                  = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(data.google_container_cluster.primary.master_auth.0.cluster_ca_certificate)
}

data "google_client_config" "default" {}
