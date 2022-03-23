# -*- coding: utf-8 -*-
# API基础
# 作者: 三石
# 时间: 2022-03-23


import uuid
from django.conf import settings
from base.utils import UtilsRequest


class ApiBase(object):

    def __init__(self):
        """
        API基础
        """
        self.zabbix_ip = settings.ZABBIX_IP
        self.zabbix_token = settings.ZABBIX_TOKEN

        self.url = "http://{}/zabbix/api_jsonrpc.php".format(self.zabbix_ip)

    def init_data(self, method: str, params: dict):
        """
        初始化data
        :param method: 方式
        :param params: 参数
        :return:
        """
        _data = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": uuid.uuid4(),
            "auth": self.zabbix_token
        }
        return _data

    def post(self, method, params):
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
        api = UtilsRequest()
        response = api.post(url=self.url, data=data)
        return response
