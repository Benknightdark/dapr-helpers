from dapr_httpx.state_api import StateApi
import asyncio
state_service = StateApi(end_point_name='statestore', timeout=4, retries=1)
print('----------刪除state------------')
s5 = state_service.delete("yo")
print(asyncio.run(s5))
print('-----------新增state-----------')
s3 = state_service.save([{"key": "yo", "value": "man"}])
print(asyncio.run(s3))
print('------------取出state----------')
s4 = state_service.get("yo")
print(asyncio.run(s4))
