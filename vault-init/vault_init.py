import boto3
import subprocess
import os
import time


## Adding 30 sec time dealy

time.sleep(30)

#### Initializing Vault

vault_init = subprocess.check_output("vault operator init -address=http://vault-server.example.com:8200", shell=True);


#### Creating AWS session to store unseal keys

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name="us-west-2"
)
try:
    response = client.create_secret(Name="Vault-Secret", Description="Vault root token and unseal keys", SecretBinary=vault_init)
    print(f" created Secret")
except ClientError as e:
    print("Unexpected error: %s" % e)
