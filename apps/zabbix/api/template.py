# -*- coding: utf-8 -*-
# API模板
# 作者: 三石
# 时间: 2022-03-28


from .base import ApiBase
from typing import Optional


class ApiTemplate(ApiBase):

    def __init__(self):
        """
        API模板
        """
        super().__init__()

    def get_detail(self, template_id: int) -> Optional[dict] == bool:
        """
        查询详情
        :param template_id: token
        :return:
        """
        response = self.post(
            method="template.get",
            params={
                "output": "extend",
                "templateids": [template_id]
            }
        )
        return response
