import logging
from dapr_httpx.dapr_api import DaprApi
from dapr_httpx.error_log_helper import format_error_msg


class StateApi(DaprApi):

    async def get_bulk_secrets(self, secret_store_name):
        return

    async def get_secert(self, secret_store_name, name):
        return
