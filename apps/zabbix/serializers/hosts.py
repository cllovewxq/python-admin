# -*- coding: utf-8 -*-
# 序列化 楼层
# 作者: 三石
# 时间: 2021-07-20


from rest_framework import serializers, validators
from zabbix.models import Hosts


class SerializersHostsIdAndName(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Hosts
        fields = ["id", "name", ]

    def get_id(self, obj):
        return obj.hostid

    def get_name(self, obj):
        return obj.name
