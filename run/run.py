# from dapr_httpx.secrets_api import SecretsApi
from dapr_httpx.invoke_api import InvokeApi
import asyncio
# service_name='api-service', timeout=4, retries=1
api_service = InvokeApi(end_point_name='api-service', timeout=4, retries=1)
# print(asyncio.run(SecretsApi(timeout=5,retries=0).get_bulk_secrets('a')))'
s1 = api_service.get('api/webpage')
print(asyncio.run(s1))
print('----------------------')
s2 = api_service.get('api/webpage')
print(asyncio.run(s2))
