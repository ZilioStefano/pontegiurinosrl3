import os
from azure.identity import EnvironmentCredential
from azure.keyvault.secrets import SecretClient

VAULT_URL = os.environ["VAULT_URL"]credential = EnvironmentCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)client.set_secret(
    "<my-password-reference>",
    "<the-actual-password>",
)