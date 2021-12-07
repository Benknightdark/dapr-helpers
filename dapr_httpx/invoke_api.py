import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class InvokeApi(DaprApi):
    """Invoke Api class

    Args:
        DaprApi (class): 繼承DaprApi
    """    

    def __init__(self, end_point_name, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        """Invoke Api class

        Args:
            end_point_name (str): api節點名稱
            timeout (int, optional): api呼叫逾時秒數。 Defaults to 30.
            retries (int, optional): api呼叫重試次數。 Defaults to 500.
            dapr_port (str, optional): dapr port number. Defaults to '3500'.
            dapr_api_version (str, optional): dapr api 版本。 Defaults to 'v1.0'.
        """
        DaprApi.__init__(self, end_point_name, timeout,
                         retries, dapr_port, dapr_api_version)
        self.invoke_url = f'{self.api_url}/invoke/{self.end_point_name}/method'

    async def get(self, method_name):
        """發送get request

        Args:
            method_name (str): api方法名稱

        Returns:
            json: 回傳api回應資料
        """        
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
        """發送post request

        Args:
            method_name (str): api方法名稱
            payload (json): 傳送給api的資料

        Returns:
            json: 回傳api回應資料
        """        
        
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
        """發送put request

        Args:
            method_name (str): api方法名稱
            payload (json): 傳送給api的資料

        Returns:
            json: 回傳api回應資料
        """  
        try:
            self.start_client()
            req = await self.client.put(f'{self.invoke_url}/{method_name}', json=payload)
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

    async def delete(self, method_name):
        """發送delete request

        Args:
            method_name (str): api方法名稱

        Returns:
            json: 回傳api回應資料
        """ 
        try:
            self.start_client()
            req = await self.client.delete(f'{self.invoke_url}/{method_name}')
            res = req.json()
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()
