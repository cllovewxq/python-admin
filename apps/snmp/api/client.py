# -*- coding: utf-8 -*-
# snmp客户端
# 作者: 三石
# 时间: 2021-10-21


import logging
import netsnmp


logger = logging.getLogger(__name__)


class ApiSnmpClient(object):

    def __init__(self, host="localhost", community="public", version=2):
        """
        snmp客户端
        """
        self.version = version
        self.host = host
        self.community = community

    def walk(self, oid) -> dict:
        """
        snmp walk
        :param oid:
        :return:
        """
        try:
            result = netsnmp.snmpwalk(
                oid,
                Version=self.version,
                DestHost=self.host,
                Community=self.community
            )
            logger.info("snmp walk 返回结果: {}".format(result))

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
