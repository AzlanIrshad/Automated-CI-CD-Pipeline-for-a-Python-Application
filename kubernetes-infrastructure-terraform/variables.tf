variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The region to deploy to"
  default     = "us-east1-b"
}

variable "cluster_name" {
  description = "The name of the GKE cluster"
  default     = "gke-test-cluster"
}
