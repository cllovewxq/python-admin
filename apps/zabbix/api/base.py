# -*- coding: utf-8 -*-
# API基础
# 作者: 三石
# 时间: 2022-03-23


import logging
import uuid
from django.conf import settings
from base.utils import UtilsRequest
from typing import Optional


logger = logging.getLogger(__name__)


class ApiBase(object):

    def __init__(self):
        """
        API基础
        """
        self.zabbix_ip = settings.ZABBIX_IP
        self.zabbix_token = settings.ZABBIX_TOKEN

        self.url = "http://{}/zabbix/api_jsonrpc.php".format(self.zabbix_ip)

        self.jsonrpc = "2.0"

    def init_data(self, method: str, params: dict) -> dict:
        """
        初始化data
        :param method: 方式
        :param params: 参数
        :return:
        """
        _data = {
            "jsonrpc": self.jsonrpc,
            "method": method,
            "params": params,
            "id": str(uuid.uuid4()),
            "auth": self.zabbix_token,
        }
        return _data

    def post(self, method, params) -> Optional[dict] == bool:
        """
        post请求
        :param method: 方式
        :param params: 参数
        :return:
        """
        data = self.init_data(
            method=method,
            params=params,
        )
        logger.debug("Zabbix请求参数: {}".format(data))
        api = UtilsRequest()
        response = api.post(url=self.url, data=data)
        return response
