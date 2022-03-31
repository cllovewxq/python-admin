# -*- coding: utf-8 -*-
# 转换工具类
# 作者: 三石
# 时间: 2021-11-02


from datetime import datetime


class UtilsConvert:
    def __init__(self):
        """
        转换类
        """
        self.date_time_format = "%Y-%m-%d %H:%M:%S"
        self.date_format = "%Y-%m-%d"

    def get_str_from_datetime(self, date_time):
        """
        时间格式转格式
        :param date_time: date_time格式数据
        :return:
        """
        if not date_time:
            return None
        else:
            date_time_str = datetime.strftime(date_time, self.date_time_format)
            return date_time_str

    def get_str_from_date(self, date_time):
        """
        日期格式转格式
        :param date_time: date_time格式数据
        :return:
        """
        if not date_time:
            return None
        else:
            date_time_str = datetime.strftime(date_time, self.date_format)
            return date_time_str

    def get_date_from_timestamp(self, timestamp):
        """
        日期格式转格式
        :param timestamp: 时间戳
        :return:
        """
        if not timestamp:
            return None
        else:
            date_time_str = datetime.fromtimestamp(timestamp)
            date_time = date_time_str.strftime(self.date_time_format)
            return date_time

    def compare_days(self, start_time, end_time) -> int:
        """
        毕竟计算天数差 结束时间要比开始时间大
        :param start_time: 开始时间 格式 2022-01-01
        :param end_time: 结束时间 格式 2022-01-01
        :return:
        """
        start = datetime.strptime(start_time, self.date_format)
        end = datetime.strptime(end_time, self.date_format)
        days = (end - start).days
        return days

    def compare_seconds(self, start_time, end_time) -> int:
        """
        毕竟计算秒数差 结束时间要比开始时间大
        :param start_time: 开始时间 格式 2022-01-01
        :param end_time: 结束时间 格式 2022-01-01
        :return:
        """
        start = datetime.strptime(start_time, self.date_time_format)
        end = datetime.strptime(end_time, self.date_time_format)
        seconds = (end - start).seconds
        return seconds
