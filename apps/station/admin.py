# -*- coding: utf-8 -*-
# admin 课程
# 作者: 三石
# 时间: 2022-02-15


from django.shortcuts import redirect
from django.contrib import admin, messages
from base.enums import EnumMsg
from station.models import Station
from zabbix.api import ApiHostGroup


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', )
    ordering = ('-create_time', )
    list_per_page = 20
    search_fields = ('name', )
    exclude = ('host_group', 'host_group_id', )

    def save_model(self, request, obj, form, change):

        api = ApiHostGroup()

        # 创建
        if not obj.host_group_id:
            response = api.create(name=str(obj.host_group))
        # 更新
        else:
            response = api.update(host_group_id=obj.host_group_id, name=str(obj.host_group))

        # 解析返回的host_group_id
        host_grop_id = api.get_host_group_id(response=response)

        if not host_grop_id:
            messages.warning(request, EnumMsg.ZabbixAPIError.value.format(api.error))
            return
        else:
            obj.host_group_id = host_grop_id
            obj.save()

    def delete_model(self, request, obj):

        api = ApiHostGroup()
        api.delete(host_group_ids=[obj.host_group_id])
        obj.delete()

    def delete_queryset(self, request, queryset):

        host_group_ids = []
        for obj in queryset:
            host_group_ids.append(obj.host_group_id)

        api = ApiHostGroup()
        api.delete(host_group_ids=host_group_ids)
        queryset.delete()
