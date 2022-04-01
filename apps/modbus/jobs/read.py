# -*- coding: utf-8 -*-
# 读取
# 作者: 三石
# 时间: 2022-02-07


import logging
from datetime import datetime
from base.utils import UtilsZabbix
from modbus.api import ApiModbusClient


logger = logging.getLogger(__name__)


def job_modbus_read_demo(devices: list):
    """
    modbus读取
    :return:
    """
    logger.debug("任务工作[modbus读取]执行开始...")

    for device in devices:

        utils_zabbix = UtilsZabbix()

        device_code = device.get("code")
        device_ipaddress = device.get("ipaddress")
        device_port = device.get("port")

        if not device_code or not device_ipaddress or not device_port:
            logger.error("设备数据不完整已过滤: {}".format(device))
        else:
            try:
                api = ApiModbusClient(ipaddress=device_ipaddress, port=device_port)
                response = api.read_input_registers(address=5000, count=100, unit=1)
                success = response.get("success")

                # 成功
                if success:
                    payload = response.get("payload")
                    utils_zabbix.create_payload(host=device_code, item_key="payload", item_value=payload, date_time=datetime.now().timetuple())
                # 失败
                else:
                    error = response.get("error")
                    utils_zabbix.create_payload(host=device_code, item_key="error", item_value=error, date_time=datetime.now().timetuple())

                packet = utils_zabbix.get_packet(data=utils_zabbix.data)
                utils_zabbix.send_packet(packet=packet)

            except Exception as error:
                logger.error("读取数据出错: {}".format(error))
                zabbix_payload = utils_zabbix.create_payload(host=device_code, item_key="error", item_value=str(error), date_time=datetime.now().timetuple())
                packet = utils_zabbix.get_packet(data=[zabbix_payload])
                utils_zabbix.send_packet(packet=packet)

    logger.debug("任务工作[modbus读取]执行结束...")
