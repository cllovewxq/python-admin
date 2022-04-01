# -*- coding: utf-8 -*-
# 视图 SNMP walk
# 作者: 三石
# 时间: 2022-02-21


import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from base.enums import EnumCode, EnumMsg
from snmp.api import ApiSnmpClient


logger = logging.getLogger(__name__)


class SnmpWalkAPIView(APIView):

    def get(self, request, *args, **kwargs):
        logger.info("Get请求信息: {}".format(request.query_params))

        api = ApiSnmpClient()
        api.walk(host="172.16.3.41", community="admin@snmp", oid="ifIndex")

        return Response(data={"code": EnumCode.Success.value})

    def post(self, request):
        return Response(data={"code": EnumCode.Success.value})

