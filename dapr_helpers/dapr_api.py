import httpx


class DaprApi:
    api_url = 'http://localhost:3500'
    client = None

    def __init__(self, timeout=30, retries=500):
        self.timeout = timeout
        self.retries = retries
        self.client = httpx.AsyncClient(
            timeout=self.timeout, transport=httpx.AsyncHTTPTransport(retries=self.retries))
