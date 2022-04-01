# -*- coding: utf-8 -*-
# snmp客户端
# 作者: 三石
# 时间: 2021-10-21


import logging
import netsnmp


logger = logging.getLogger(__name__)


class ApiSnmpClient(object):

    def __init__(self):
        """
        snmp客户端
        """
        self.version = 2

    def walk(self, host, community, oid) -> dict:
        """
        snmp walk
        :param host: 主机IP
        :param community: 共同体名
        :param oid:
        :return:
        """
        try:
            result = netsnmp.snmpwalk(
                oid,
                Version=self.version,
                DestHost=host,
                Community=community
            )
            logger.debug("snmp walk 返回结果: {}".format(result))

            return {
                "success": True,
                "result": result
            }

        except Exception as e:
            logger.error("snmp walk 发生异常: {}".format(e))
            return {
                "success": False,
                "error": str(e)
            }
