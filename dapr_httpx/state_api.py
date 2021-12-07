import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class StateApi(DaprApi):
    def __init__(self, end_point_name, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        DaprApi.__init__(self, end_point_name, timeout,
                         retries, dapr_port, dapr_api_version)
        self.state_url = f'{self.api_url}/state/{self.end_point_name}'

    async def get(self, key):
        '''
        取得某一個state key的資料
        '''
        try:
            self.start_client()
            req = await self.client.get(f'{self.state_url}/{key}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def save(self, key):
        '''
        儲存某一個state key的資料
        '''
        try:
            self.start_client()
            req = await self.client.post(f'{self.state_url}/{key}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def delete(self, key):
        '''
        刪除某一個state key的資料
        '''
        try:
            self.start_client()
            req = await self.client.delete(f'{self.state_url}/{key}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def bulk(self, payload=None):
        '''
        批次取得secret store的全部資料
        '''
        try:
            self.start_client()
            req = await self.client.post(f'{self.state_url}/bulk', json=payload)
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()
