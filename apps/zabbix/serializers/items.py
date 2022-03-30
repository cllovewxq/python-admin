# -*- coding: utf-8 -*-
# 序列化
# 作者: 三石
# 时间: 2021-07-20


from rest_framework import serializers, validators
from zabbix.models import Items


class SerializersItemsIdAndName(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ["id", "name", "value_type", ]

    def get_id(self, obj):
        return obj.itemid

    def get_name(self, obj):
        return obj.name
