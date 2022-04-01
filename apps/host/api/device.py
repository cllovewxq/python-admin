# -*- coding: utf-8 -*-
# API设备
# 作者: 三石
# 时间: 2022-03-28


import logging
from typing import Optional
from base.enums import EnumDeviceType
from host.models import Switch


logger = logging.getLogger(__name__)


class ApiDevice(object):

    def __init__(self):
        """
        API设备
        """
        super().__init__()

    def get(self, zabbix_id, zabbix_code) -> Optional[dict] == bool:
        """
        查询
        :return:
        """
        logger.debug(self.__doc__)

        switch = Switch.objects.filter(zabbix_id=zabbix_id, zabbix_code=zabbix_code).exists()
        if switch:
            db_device = Switch.objects.get(zabbix_id=zabbix_id, zabbix_code=zabbix_code)
            return {
                "device_type": EnumDeviceType.switch.name,
                "device_id": db_device.id,
                "device_code": db_device.code,
            }

        return False

    def get_name_from_type(self, device_type, zabbix_id, zabbix_code) -> Optional[str] == bool:
        """
        查询
        :return:
        """
        logger.debug(self.__doc__)

        if device_type == EnumDeviceType.switch.name:
            switch = Switch.objects.filter(zabbix_id=zabbix_id, zabbix_code=zabbix_code).exists()
            if switch:
                db_device = Switch.objects.get(zabbix_id=zabbix_id, zabbix_code=zabbix_code)
                return db_device.name
        return False

    def get_station_name_from_type(self, device_type, zabbix_id, zabbix_code) -> Optional[str] == bool:
        """
        查询
        :return:
        """
        logger.debug(self.__doc__)

        if device_type == EnumDeviceType.switch.name:
            switch = Switch.objects.filter(zabbix_id=zabbix_id, zabbix_code=zabbix_code).exists()
            if switch:
                db_device = Switch.objects.get(zabbix_id=zabbix_id, zabbix_code=zabbix_code)
                return db_device.station.name
        return False
