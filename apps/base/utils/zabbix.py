# -*- coding: utf-8 -*-
# zabbix工具类
# 作者: 三石
# 时间: 2021-07-01


import logging
import socket
import struct
import json
import time
from django.conf import settings


logger = logging.getLogger(__name__)


class UtilsZabbix(object):

    def __init__(self):
        """
        zabbix工具类
        """
        self.logger = logger
        self.host = settings.ZABBIX_IP
        self.port = int(settings.ZABBIX_PORT)

        self.header_protocol = "ZBXD"

        self.data = []

    @property
    def header(self):
        """
        信息头
        :return:
        """
        flags = "\1"
        header = (self.header_protocol + flags).encode("utf-8")
        return header

    def get_packet(self, data):
        """
        请求包
        :param data: 消息内容
        :return:
        """
        packet = {
            "request": "sender data",
            "data": data
        }
        # json转str
        packet = json.dumps(packet, ensure_ascii=False).encode("utf-8")

        packet_len = struct.pack("<Q", len(packet))

        # 拼接
        request_packet = self.header + packet_len + packet
        return request_packet

    def send_packet(self, packet):
        """
        发送报文
        :param packet: 请求包
        :return:
        """
        self.logger.info("开始连接socket...")
        self.logger.debug("数据包: {}".format(packet))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # 设置超时
            sock.settimeout(10)
            sock.connect((self.host, self.port))

            self.logger.info("连接成功,开始发送数据包")
            # 发送请求
            sock.sendall(packet)

            # 获取返回头
            response_header = sock.recv(13)

            packet_len = struct.unpack("<Q", response_header[len(self.header):])[0]
            response_packet = sock.recv(packet_len)

            self.logger.info("返回数据包：{}".format(response_packet))
            sock.close()

            # 获取socket返回包里的info字段 并去除空格
            info = json.loads(response_packet)["info"].replace(" ", "")

            # 拼接info组装detail
            detail = {}
            for item in info.split(";"):
                group = item.split(":")
                detail[group[0]] = group[1]

            self.logger.info("返回信息：{}".format(detail))
            return detail

        # 拦截异常
        except socket.timeout as e:
            sock.close()
            self.logger.error("出现异常,异常信息：{}".format(str(e)))
            return str(e)

        except OSError as e:
            sock.close()
            self.logger.error("出现异常,异常信息：{}".format(str(e)))
            return str(e)

        except Exception as e:
            sock.close()
            self.logger.error("出现异常,异常信息：{}".format(str(e)))
            return str(e)

    def create_payload(self, host, item_key, item_value, date_time):
        """
        新增数据源
        :param host: 主机名称
        :param item_key: 监控项key
        :param item_value: 监控项值
        :param date_time: 采集时间
        :return:
        """
        self.logger.debug("zabbix数据时间: {}".format(date_time))
        payload = {
            "host": str(host),
            "key": item_key,
            "value": json.dumps(item_value, ensure_ascii=False),
            "clock": int(time.mktime(date_time)),
        }

        # 拼接报文
        self.data.append(payload)
        return payload

    @property
    def clock(self):
        """
        当前时间戳
        :return:
        """
        return int(time.time())
