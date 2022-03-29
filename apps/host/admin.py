# -*- coding: utf-8 -*-
# admin
# 作者: 三石
# 时间: 2022-02-15


from django.http import HttpResponseRedirect
from django.contrib import admin, messages
from base.enums import EnumMsg
from host.models import Switch
from zabbix.api import ApiHost


@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):

    list_display = ('code', 'name', 'station', 'model_id', 'status_operation', 'create_time', )
    ordering = ('-create_time', )
    list_per_page = 20
    list_filter = ['model_id', ]
    search_fields = ('name', )
    exclude = ['host', 'host_id', 'status', ]

    def response_add(self, request, obj, post_url_continue=None):
        if messages.get_messages(request):
            return HttpResponseRedirect(".")
        return super(SwitchAdmin, self).response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        if messages.get_messages(request):
            return HttpResponseRedirect(".")
        return super(SwitchAdmin, self).response_change(request, obj)

    def save_model(self, request, obj, form, change):

        api = ApiHost()

        # 创建
        if not obj.host_id:
            response = api.create_snmp(
                name=obj.name,
                host=str(obj.host),
                group_id=obj.station.host_group_id,
                model_id=obj.model_id,
                ipaddress=obj.ipaddress,
                port=obj.port,
                snmp_community=obj.snmp_community,
            )
        # 更新
        else:
            response = api.update_snmp(
                host_id=obj.host_id,
                name=obj.name,
                group_id=obj.station.host_group_id,
                model_id=obj.model_id,
                ipaddress=obj.ipaddress,
                port=obj.port,
                snmp_community=obj.snmp_community,
            )

        # 解析返回的host_id
        host_id = api.get_host_id(response=response)

        if not host_id:
            messages.warning(request, EnumMsg.ZabbixAPIError.value.format(api.error))
            return
        else:
            obj.host_id = host_id
            obj.save()

    def delete_model(self, request, obj):

        api = ApiHost()
        api.delete(host_ids=[obj.host_id])
        obj.delete()

    def delete_queryset(self, request, queryset):

        host_ids = []
        for obj in queryset:
            host_ids.append(obj.host_id)

        api = ApiHost()
        api.delete(host_ids=host_ids)
        queryset.delete()
