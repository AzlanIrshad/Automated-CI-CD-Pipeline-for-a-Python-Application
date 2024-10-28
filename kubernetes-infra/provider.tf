provider "google" {
 #credentials provide path to key
  project = "gcp-deployment-439420"
  region  = "us-east1-b"
}

data "google_container_cluster" "primary" {
  name     = "gke-test-cluster"
  location = "us-east1-b"
}


provider "kubernetes" {
  host                   = "https://34.148.98.108"
  token                  = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(data.google_container_cluster.primary.master_auth.0.cluster_ca_certificate)
}

data "google_client_config" "default" {}
