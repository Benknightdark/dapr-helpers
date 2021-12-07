import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class SecretsApi(DaprApi):
    '''
    Secrets API
    '''

    def __init__(self, end_point_name, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        DaprApi.__init__(self, end_point_name, timeout,
                         retries, dapr_port, dapr_api_version)
        self.secrets_url=f'{self.api_url}/secrets/{self.end_point_name}'
    async def get_bulk_secrets(self):
        '''
        批次取得秘密資料
        '''
        try:
            self.start_client()
            req = await self.client.get(f'{self.secrets_url}/bulk')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def get_secert(self, name):
        '''
        根據秘密儲存庫名稱取得對應的秘密資料
        '''
        try:
            self.start_client()
            req = await self.client.get(f'{self.secrets_url}/{name}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()
