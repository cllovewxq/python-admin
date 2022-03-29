# -*- coding: utf-8 -*-
# API主机接口
# 作者: 三石
# 时间: 2022-03-28


from .base import ApiBase
from typing import Optional


class ApiHostInterface(ApiBase):

    def __init__(self):
        """
        API主机接口
        """
        super().__init__()

    def get_detail(self, host_id: int) -> Optional[dict] == bool:
        """
        查询详情
        :param host_id: 主机ID
        :return:
        """
        response = self.post(
            method="hostinterface.get",
            params={
                "output": "extend",
                "hostids": host_id
            }
        )
        return response
