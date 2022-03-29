# -*- coding: utf-8 -*-
# 枚举code
# 作者: 三石
# 时间: 2021-07-09


from enum import Enum, unique


@unique
class EnumCode(Enum):
    """
    枚举code
    """

    Success = 10000
    Error = 50000

    InvalidError = 61000
    InvalidParam = 61001
    NotFound = 61002
    AlreadyExists = 61003
    PermissionDenied = 61004

    MethodNotSupport = 63000

    UnknownError = 64000
    AuthFailed = 64001
    AuthError = 64003
    UrlNotFound = 6004

    KnownError = 65000
    KnownErrorNotExist = 65001
    KnownErrorWechat = 65002

    KnownErrorNoVIP = 65101
    KnownErrorNoBuy = 65102
    KnownErrorNoEnrollment = 65103

    KnownErrorGiveLevelNotMatch = 65201
    KnownErrorGiveUsed = 65202
    KnownErrorGiveNotFound = 65203


