# -*- coding: utf-8 -*-
# API主机组
# 作者: 三石
# 时间: 2022-03-28


from .base import ApiBase
from typing import Optional
from base.enums import EnumMsg


class ApiHostGroup(ApiBase):

    def __init__(self):
        """
        API主机组
        """
        super().__init__()

    def get_list(self) -> Optional[dict] == bool:
        """
        查询所有
        :return:
        """
        response = self.post(
            method="hostgroup.get",
            params={

            }
        )
        return response

    def create(self, name) -> Optional[dict] == bool:
        """
        创建
        :param name: 名称
        :return:
        """
        response = self.post(
            method="hostgroup.create",
            params={
                "name": name,
            }
        )
        return response

    def update(self, host_group_id, name) -> Optional[dict] == bool:
        """
        更新
        :param host_group_id: ID
        :param name: 名称
        :return:
        """
        response = self.post(
            method="hostgroup.update",
            params={
                "groupid": host_group_id,
                "name": name,
            }
        )
        return response

    def delete(self, host_group_ids: list) -> Optional[dict] == bool:
        """
        删除
        :param host_group_ids: ID数组
        :return:
        """
        response = self.post(
            method="hostgroup.delete",
            params=host_group_ids
        )
        return response

    @staticmethod
    def get_host_group_id(response) -> Optional[bool] == str:
        """
        查询主机组ID
        """
        result = response.get("result", {})
        group_ids = result.get("groupids", [])
        if not group_ids:
            error = response.get("error", {})
            data = error.get("data", EnumMsg.UnknownError.value)
            return data
        else:
            return group_ids[0]

