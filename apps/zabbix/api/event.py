# -*- coding: utf-8 -*-
# API事件
# 作者: 三石
# 时间: 2022-03-28


from .base import ApiBase
from typing import Optional


class ApiEvent(ApiBase):

    def __init__(self):
        """
        API事件
        """
        super().__init__()

    def update_acknowledge(self, event_id: int) -> Optional[dict] == bool:
        """
        更新确认
        :param event_id: 事件ID
        :return:
        """
        response = self.post(
            method="event.acknowledge",
            params={
                "eventids": event_id,
                "action": 2,
            }
        )
        return response
