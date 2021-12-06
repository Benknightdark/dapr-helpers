import httpx


class DaprApi:
    def __init__(self, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        self.timeout = timeout
        self.retries = retries
        self.api_url = f'http://localhost:{dapr_port}/{dapr_api_version}'
        self.client = None

    def start_client(self):
        '''
        啟動httpx client
        '''
        self.client = httpx.AsyncClient(
            timeout=self.timeout, transport=httpx.AsyncHTTPTransport(retries=self.retries))

    async def close_client(self):
        '''
        關閉httpx client
        '''
        await self.client.aclose()
