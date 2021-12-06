import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class InvokeApi(DaprApi):
    '''
    Service invocation API
    '''
    def __init__(self,service_name, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        DaprApi.__init__(self,timeout,retries,dapr_port,dapr_api_version)
        self.invoke_url = f'{self.api_url}/invoke/{service_name}/method'

    async def get(self, method_name):
        '''
        發送get request
        '''
        try:
            self.start_client()
            req = await self.client.get(f'{self.invoke_url}/{method_name}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def post(self, method_name, payload):
        '''
        發送post request
        '''
        try:
            self.start_client()
            req = await self.client.post(f'{self.invoke_url}/{method_name}', json=payload)
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def put(self, method_name, payload):
        '''
        發送put request
        '''
        try:
            self.start_client()
            req = await self.client.put(f'{self.invoke_url}/{method_name}', json=payload)
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def delete(self, method_name, payload):
        '''
        發送delete request
        '''
        try:
            self.start_client()
            req = await self.client.delete(f'{self.invoke_url}/{method_name}', json=payload)
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()
