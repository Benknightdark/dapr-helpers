import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class StateApi(DaprApi):
    """State Api class

    Args:
        DaprApi (class): 繼承DaprApi
    """

    def __init__(self, end_point_name, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        """State Api class

        Args:
            end_point_name (str): api節點名稱
            timeout (int, optional): api呼叫逾時秒數。 Defaults to 30.
            retries (int, optional): api呼叫重試次數。 Defaults to 500.
            dapr_port (str, optional): dapr port number. Defaults to '3500'.
            dapr_api_version (str, optional): dapr api 版本。 Defaults to 'v1.0'.
        """
        DaprApi.__init__(self, end_point_name, timeout,
                         retries, dapr_port, dapr_api_version)
        self.state_url = f'{self.api_url}/state/{self.end_point_name}'

    async def get(self, key):
        """ 取得某一個state key的資料

        Args:
            key (str): state key名稱

        Returns:
            json: state的資料
        """
        try:
            self.start_client()
            req = await self.client.get(f'{self.state_url}/{key}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def save(self, payload):
        """儲存state資料

        Args:
            payload (json): 要儲存至state的資料
        Returns:
            str: http status code
        """
        try:
            self.start_client()
            req = await self.client.post(f'{self.state_url}', json=payload)
            res = req.status_code
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def delete(self, key):
        """刪除某一個state key的資料

        Args:
            key (str): state key名稱

        Returns:
            str: http status code
        """
        try:
            self.start_client()
            req = await self.client.delete(f'{self.state_url}/{key}')
            res = req.status_code
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def bulk(self, payload=None):
        """批次取得secret store的全部資料


        Args:
            payload (json, optional): 批次查詢資料的參數。 Defaults to None.

        Returns:
            json: 回傳查詢的資料
        """
        try:
            self.start_client()
            req = await self.client.post(f'{self.state_url}/bulk', json=payload)
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()
