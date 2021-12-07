import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class StateApi(DaprApi):
    def __init__(self, end_point_name, timeout=30, retries=500, dapr_port='3500', dapr_api_version='v1.0'):
        DaprApi.__init__(self, end_point_name, timeout,
                         retries, dapr_port, dapr_api_version)
        self.state_url=f''