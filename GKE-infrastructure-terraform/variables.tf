variable "project_id" {
    description = "This is the project name"
    type = string
}
variable "region" {
  description = "This is the region"
  default = "us-east1-b"
}
variable "cluster_name" {
  description = "This is the cluster name"
  default = "gke-test-cluster"
}
