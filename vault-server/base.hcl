storage "dynamodb" {
  ha_enabled = "true"
  region     = "us-west-2"
  table      = "vault-data"
}
listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_disable = "true"
}
seal "awskms" {
  region = "us-west-2"
  kms_key_id = "xxxxx-xxxx-xxxxx"
}
ui=true
disable_mlock = true
api_addr = "http://127.0.0.1:8200"
