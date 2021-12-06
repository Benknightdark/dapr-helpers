import httpx


class DaprApi:
    def __init__(self, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        self.timeout = timeout
        self.retries = retries
        self.api_url = f'http://localhost:{dapr_port}/{dapr_api_version}'
        self.client = httpx.AsyncClient(
            timeout=self.timeout, transport=httpx.AsyncHTTPTransport(retries=self.retries))
