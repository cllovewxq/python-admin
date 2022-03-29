# -*- coding: utf-8 -*-
# 枚举msg
# 作者: 三石
# 时间: 2021-07-09


from enum import Enum, unique


@unique
class EnumMsg(Enum):
    """
    枚举code
    """

    Success = "请求成功"
    Error = "请求失败"

    InvalidError = "请求参数错误"
    InvalidParam = "请求参数无效"
    NotFound = "数据不存在"
    AlreadyExists = "数据已存在"
    PermissionDenied = "数据权限不足"

    MethodNotSupport = "{}请求方法不支持"

    UnknownError = "服务未知异常,详情查看日志"
    AuthFailed = "认证失败,请重新登录"
    AuthStatusError = "认证状态异常"
    UrlNotFound = "请求url不存在"

    UserNotConfiguredToken = "用户未配置Token"
    ZabbixAPIError = "Zabbix接口服务异常: {}"

    SuccessEnable = "数据启用成功"
    SuccessDisable = "数据禁用成功"
