# -*- coding: utf-8 -*-
# 视图
# 作者: 三石
# 时间: 2021-07-09


import logging
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework.views import APIView
from base.enums import EnumMsg
from host.models import Switch
from zabbix.api import ApiHost


logger = logging.getLogger(__name__)


class SwitchEnableAPIView(APIView):
    """
    启用
    """
    def get(self, request, switch_id, *args, **kwargs):

        switch = Switch.objects.filter(id=switch_id).exists()
        if not switch:
            messages.warning(request, EnumMsg.NotFound.value)
            return redirect("/admin/host/switch/")

        db_switch = Switch.objects.get(id=switch_id)

        api = ApiHost()
        api.enable(host_id=db_switch.host_id)

        db_switch.status = Switch.StatusChoices.enable.name
        db_switch.save(update_fields=["status"])

        messages.success(request, EnumMsg.SuccessEnable.value)
        return redirect("/admin/host/switch/")

    def post(self, request, *args, **kwargs):
        messages.info(request, EnumMsg.MethodNotSupport.value.format("POST"))
        return redirect("/admin/host/switch/")


class SwitchDisableAPIView(APIView):
    """
    禁用
    """
    def get(self, request, switch_id, *args, **kwargs):

        switch = Switch.objects.filter(id=switch_id).exists()
        if not switch:
            messages.warning(request, EnumMsg.NotFound.value)
            return redirect("/admin/host/switch/")

        db_switch = Switch.objects.get(id=switch_id)

        api = ApiHost()
        api.disable(host_id=db_switch.host_id)

        db_switch.status = Switch.StatusChoices.disable.name
        db_switch.save(update_fields=["status"])

        messages.success(request, EnumMsg.SuccessDisable.value)
        return redirect("/admin/host/switch/")

    def post(self, request, *args, **kwargs):
        messages.info(request, EnumMsg.MethodNotSupport.value.format("POST"))
        return redirect("/admin/host/switch/")
