import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class PubSubApi(DaprApi):
    """Pub/Sub Api class

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
        self.pubsub_url = f'{self.api_url}/publish/{self.end_point_name}'

    async def publish(self, topic,payload):
        """發送訊息給指定的主題

        Args:
            topic (str): 主題名稱
            payload (json): 傳送給主題的訊息資料

        Returns:
            str: 回傳http status code
        """        
        try:
            self.start_client()
            req = await self.client.post(f'{self.pubsub_url}/{topic}',json=payload)
            res = req.status_code
            return res
        except Exception as e:
            logging.error(format_error_msg(e))
        finally:
            await self.close_client()

   