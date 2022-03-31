# -*- coding: utf-8 -*-
# 枚举设备类型
# 作者: 三石
# 时间: 2021-07-09


from enum import Enum, unique


@unique
class EnumDeviceType(Enum):
    """设备类型"""

    switch = "交换机"
