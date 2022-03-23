# -*- coding: utf-8 -*-
# 接口工具类
# 作者: 三石
# 时间: 2021-11-16


import httpx
import json
import logging


logger = logging.getLogger(__name__)


class UtilsRequest(object):

    def __init__(self):
        """
        接口工具类
        """
        # 超时时间
        self.timeout = 5

        self.response = False

    def get(self, url, headers=None, params=None):
        """
        get请求
        :param url: 地址
        :param headers: 请求头
        :param params: 请求参数
        :return:
        """
        if headers is None:
            headers = {}
        if params is None:
            params = {}

        # json转str
        headers_str = json.dumps(headers, ensure_ascii=False)
        params_str = json.dumps(params, ensure_ascii=False)
        logger.info("调用Get请求,地址: {url}, 信息头: {headers}, 参数: {params}".format(url=url, headers=headers_str, params=params_str))

        try:
            response = httpx.get(url=url, headers=headers, params=params, timeout=self.timeout, verify=False)
            self.response = response.json()

            logger.info("调用返回: {}".format(self.response))
            return True
        except httpx.RequestError as error:
            logger.error("接口请求错误: {}".format(error))
            return False

    def post(self, url, headers=None, params=None, data=None):
        """
        post请求
        :param url: 地址
        :param headers: 请求头
        :param params: 请求参数
        :param data: 请求报文
        :return:
        """
        if headers is None:
            headers = {}
        if data is None:
            data = {}

        # json转str
        headers_str = json.dumps(headers, ensure_ascii=False)
        params_str = json.dumps(params, ensure_ascii=False)
        data_str = json.dumps(data, ensure_ascii=False)
        logger.info("调用post请求,地址: {url}, 信息头: {headers}, 参数: {data}".format(url=url, headers=headers_str,  params=params_str, data=data_str))

        try:
            response = httpx.post(url=url, headers=headers, params=params, json=data, timeout=self.timeout, verify=False)
            self.response = response.json()
            logger.info("调用返回: {}".format(self.response))
            return True
        except httpx.RequestError as error:
            logger.error("接口请求错误: {}".format(error))
            return False
