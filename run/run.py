# from dapr_httpx.secrets_api import SecretsApi
from dapr_httpx.invoke_api import InvokeApi
import asyncio
api_service=InvokeApi()
# print(asyncio.run(SecretsApi(timeout=5,retries=0).get_bulk_secrets('a')))
print(asyncio.run(api_service.get('/api-service/api/webpage')))