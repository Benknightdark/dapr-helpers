import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class InvokeApi(DaprApi):
    '''
    Service invocation API
    '''
    #def __init__(self):
        # self.invoke_url = f'{self.api_url}/invoke/method'

    async def get(self, method_name):
        '''
        發送get request
        '''
        try:
            print(self.api_url)
            req = await self.client.get(f'{self.api_url}/invoke/method/{method_name}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.client.aclose()

    # async def post(self, method_name, payload):
    #     '''
    #     發送post request
    #     '''
    #     try:
    #         req = await self.client.post(f'{self.invoke_url}/{method_name}', json=payload)
    #         res = req.json()
    #         return res
    #     except Exception as e:
    #         logging.error(format_error_msg(e))
    #     finally:
    #         await self.client.aclose()

    # async def put(self, method_name, payload):
    #     '''
    #     發送put request
    #     '''
    #     try:
    #         req = await self.client.put(f'{self.invoke_url}/{method_name}', json=payload)
    #         res = req.json()
    #         return res
    #     except Exception as e:
    #         logging.error(format_error_msg(e))
    #     finally:
    #         await self.client.aclose()

    # async def delete(self, method_name, payload):
    #     '''
    #     發送delete request
    #     '''
    #     try:
    #         req = await self.client.delete(f'{self.invoke_url}/{method_name}', json=payload)
    #         res = req.json()
    #         return res
    #     except Exception as e:
    #         logging.error(format_error_msg(e))
    #     finally:
    #         await self.client.aclose()
