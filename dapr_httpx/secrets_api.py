import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class SecretsApi(DaprApi):
    """Secrets Api class

    Args:
        DaprApi (class): 繼承DaprApi
    """

    def __init__(self, end_point_name, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        """Secrets Api class

        Args:
            end_point_name (str): api節點名稱
            timeout (int, optional): api呼叫逾時秒數。 Defaults to 30.
            retries (int, optional): api呼叫重試次數。 Defaults to 500.
            dapr_port (str, optional): dapr port number. Defaults to '3500'.
            dapr_api_version (str, optional): dapr api 版本。 Defaults to 'v1.0'.
        """
        DaprApi.__init__(self, end_point_name, timeout,
                         retries, dapr_port, dapr_api_version)
        self.secrets_url = f'{self.api_url}/secrets/{self.end_point_name}'

    async def get_bulk_secrets(self):
        """批次取得秘密資料

        Returns:
            json: 回傳查詢的資料
        """        
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
        """ 根據名稱取得對應的秘密資料

        Args:
            name (str): 秘密資料的名稱

        Returns:
            json: 回傳查詢的資料
        """        
        try:
            self.start_client()
            req = await self.client.get(f'{self.secrets_url}/{name}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()
