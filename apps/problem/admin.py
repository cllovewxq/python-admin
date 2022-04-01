# -*- coding: utf-8 -*-
# admin
# 作者: 三石
# 时间: 2022-02-15


from django.http import HttpResponseRedirect
from django.contrib import admin, messages
from base.enums import EnumMsg
from host.models import Switch
from problem.models import Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):

    list_display = ('event_id', 'level', 'device_code', 'device_name', 'name', 'ack_status_operation', 'status_value', 'trigger_time')
    ordering = ('-trigger_time', )
    list_per_page = 20
    list_filter = ['device_code', 'status', 'trigger_time', ]
    search_fields = ('name', )

    exclude = ['zabbix_id', 'zabbix_code', ]

    # fields = ['create_time', ]

    fieldsets = (
        ("设备信息", {
            'fields': ('device_type', 'device_code', 'device_station', 'device_name', )
        }),
        ("告警消息", {
            'fields': ('event_id', 'level', 'name', 'ack_status', 'status', 'trigger_time', 'solve_time', )
        })
    )

    def has_change_permission(self, request, obj=None):
        return False
