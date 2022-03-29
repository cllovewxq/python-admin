# -*- coding: utf-8 -*-
# API主机
# 作者: 三石
# 时间: 2022-03-28


from .base import ApiBase
from .hostinterface import ApiHostInterface
from typing import Optional
from base.enums import EnumMsg


class ApiHost(ApiBase):

    def __init__(self):
        """
        API主机
        """
        super().__init__()

    def get_list(self) -> Optional[dict] == bool:
        """
        查询所有
        :return:
        """
        response = self.post(
            method="host.get",
            params={

            }
        )
        return response

    def enable(self, host_id):
        """
        启用
        :param host_id: 主机ID
        :return:
        """
        response = self.post(
            method="host.update",
            params={
                "hostid": host_id,
                "status": 0
            }
        )
        return response

    def disable(self, host_id):
        """
        禁用
        :param host_id: 主机ID
        :return:
        """
        response = self.post(
            method="host.update",
            params={
                "hostid": host_id,
                "status": 1
            }
        )
        return response

    def create_snmp(self, host, name, group_id, model_id, ipaddress, port, snmp_community) -> Optional[dict] == bool:
        """
        创建SNMP
        :param host: 编号
        :param name: 名称
        :param group_id: 主机组ID
        :param model_id: 模板ID
        :param ipaddress: IP地址
        :param port: 端口
        :param snmp_community: SNMP共同体名
        :return:
        """
        response = self.post(
            method="host.create",
            params={
                "host": host,
                "name": name,
                "interfaces": [
                    {
                        "type": 2,
                        "main": 1,
                        "useip": 1,
                        "ip": ipaddress,
                        "dns": "",
                        "port": port,
                        "details": {
                            "version": 2,
                            "community": snmp_community
                        }
                    }
                ],
                "groups": [
                    {
                        "groupid": group_id
                    }
                ],
                "templates": [
                    {
                        "templateid": model_id
                    }
                ],
            }
        )
        return response

    def update_snmp(self, host_id, name, group_id, model_id, ipaddress, port, snmp_community) -> Optional[dict] == bool:
        """
        更新SNMP
        :param host_id: ID
        :param name: 名称
        :param group_id: 主机组ID
        :param model_id: 模板ID
        :param ipaddress: IP地址
        :param port: 端口
        :param snmp_community: SNMP共同体名
        :return:
        """
        response_host_interface = ApiHostInterface().get_detail(host_id=host_id)
        result = response_host_interface.get("result", [])
        if not result:
            params_interface = {
                "type": 2,
                "main": 1,
                "useip": 1,
                "ip": ipaddress,
                "dns": "",
                "port": port,
                "details": {
                    "version": 2,
                    "community": snmp_community
                }
            }
        else:
            params_interface = {
                "interfaceid": result[0].get("interfaceid"),
                "type": 2,
                "main": 1,
                "useip": 1,
                "ip": ipaddress,
                "dns": "",
                "port": port,
                "details": {
                    "version": 2,
                    "community": snmp_community
                }
            }

        response = self.post(
            method="host.update",
            params={
                "hostid": host_id,
                "name": name,
                "interfaces": [
                    params_interface
                ],
                "groups": [
                    {
                        "groupid": group_id
                    }
                ],
                "templates": [
                    {
                        "templateid": model_id
                    }
                ],
            }
        )
        return response

    def delete(self, host_ids: list) -> Optional[dict] == bool:
        """
        删除
        :param host_ids: ID数组
        :return:
        """
        response = self.post(
            method="host.delete",
            params=host_ids
        )
        return response

    def get_host_id(self, response) -> Optional[bool] == str:
        """
        查询主机ID
        """
        result = response.get("result", {})
        host_ids = result.get("hostids", [])
        if not host_ids:
            error = response.get("error", {})
            data = error.get("data", EnumMsg.UnknownError.value)
            self.error = data
            return False
        else:
            return host_ids[0]
