# -*- coding: utf-8 -*-
# API历史
# 作者: 三石
# 时间: 2022-03-28


from .base import ApiBase
from typing import Optional


class ApiHistory(ApiBase):

    def __init__(self):
        """
        API历史
        """
        super().__init__()

    def get(self, host_id: int, item_ids: list) -> Optional[dict] == bool:
        """
        查询
        :param host_id: 主机ID
        :param item_ids: 监控项ID数组
        :return:
        """
        response = self.post(
            method="history.get",
            params={
                "output": "extend",
                "hostids": host_id,
                "itemids": item_ids,
                "sortfield": "itemid",
                "sortorder": "DESC",
                "limit": len(item_ids)
            }
        )
        return response
