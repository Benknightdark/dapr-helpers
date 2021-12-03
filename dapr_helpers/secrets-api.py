import httpx
api_url='http://localhost:3500'
async def get_bulk_secrets(secret_store_name):
    req=await httpx.AsyncClient().get(f'{api_url}/v1.0/secrets/{secret_store_name}/bulk')
    res=req.json()
    return res
async def get_secert(secret_store_name,name):
    req=await httpx.AsyncClient().get(f'{api_url}/v1.0/secrets/{secret_store_name}/{name}')
    res=req.json()
    return res    