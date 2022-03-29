# -*- coding: utf-8 -*-
# admin
# 作者: 三石
# 时间: 2022-02-15


from django.http import HttpResponseRedirect
from django.contrib import admin, messages
from django.shortcuts import render
from base.enums import EnumMsg
from history.models import History
from zabbix.api import ApiHost


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        context = {"data": []}
        return render(request, 'history.html', context)
