import httpx


class DaprApi:
    """Dapr Api class
    """
    def __init__(self, end_point_name, timeout, retries, dapr_port, dapr_api_version):
        """Dapr Api class

        Args:
            end_point_name (str): api節點名稱
            timeout (int): api呼叫逾時秒數
            retries (int): api呼叫重試次數
            dapr_port (str): dapr port number
            dapr_api_version (str): dapr api 版本
        """        
        self.timeout = timeout
        self.retries = retries
        self.end_point_name = end_point_name
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
