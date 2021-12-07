# from dapr_httpx.secrets_api import SecretsApi
from dapr_httpx.invoke_api import InvokeApi
from dapr_httpx.state_api import StateApi
import asyncio
# service_name='api-service', timeout=4, retries=1
api_service = InvokeApi(end_point_name='api-service', timeout=4, retries=1)
state_service = StateApi(end_point_name='statestore', timeout=4, retries=1)

# print(asyncio.run(SecretsApi(timeout=5,retries=0).get_bulk_secrets('a')))'
s1 = api_service.get('api/webpage')
print(asyncio.run(s1))
print('----------------------')
s2 = api_service.get('api/webpage')
print(asyncio.run(s2))
print('----------------------')
s5=state_service.delete("yo")
print(asyncio.run(s5))
print('----------------------')
s3=state_service.save([{"key":"yo","value":"man"}])
print(asyncio.run(s3))
print('----------------------')
s4=state_service.get("yo")
print(asyncio.run(s4))