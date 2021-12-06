import logging
from dapr_helpers.dapr_api import DaprApi
from dapr_helpers.error_log_helper import format_error_msg


class SecretsApi(DaprApi):

    async def get_bulk_secrets(self, secret_store_name):
        '''
        批次取得秘密資料
        '''
        try:
            req = await self.client.get(f'{self.api_url}/v1.0/secrets/{secret_store_name}/bulk')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.client.aclose()

    async def get_secert(self, secret_store_name, name):
        '''
        根據秘密儲存庫名稱取得對應的秘密資料
        '''
        try:
            req = await self.client.get(f'{self.api_url}/v1.0/secrets/{secret_store_name}/{name}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.client.aclose()
