from dapr_helpers.secrets_api import SecretsApi
import asyncio

asyncio.run(SecretsApi(timeout=5,retries=0).get_bulk_secrets('a'))