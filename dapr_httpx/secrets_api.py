import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class SecretsApi(DaprApi):
    '''
    Secrets API
    '''

    def __init__(self):
        DaprApi.__init__(self)

    async def get_bulk_secrets(self, secret_store_name):
        '''
        批次取得秘密資料
        '''
        try:
            self.start_client()
            req = await self.client.get(f'{self.api_url}/secrets/{secret_store_name}/bulk')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def get_secert(self, secret_store_name, name):
        '''
        根據秘密儲存庫名稱取得對應的秘密資料
        '''
        try:
            self.start_client()
            req = await self.client.get(f'{self.api_url}/secrets/{secret_store_name}/{name}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()
