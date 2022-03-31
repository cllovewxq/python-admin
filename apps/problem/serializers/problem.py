# -*- coding: utf-8 -*-
# 序列化
# 作者: 三石
# 时间: 2021-07-20


from rest_framework import serializers, validators
from problem.models import Problem


class SerializersProblemCreate(serializers.ModelSerializer):

    event_id = serializers.IntegerField()
    zabbix_id = serializers.IntegerField()
    zabbix_code = serializers.CharField(max_length=64)
    name = serializers.CharField(max_length=255)
    level = serializers.CharField(max_length=32)
    event_date = serializers.CharField(max_length=32)
    event_time = serializers.CharField(max_length=32)

    class Meta:
        model = Problem
        fields = ["event_id", "zabbix_id", "zabbix_code", "name", "level", "event_date", "event_time"]

    def validate(self, attrs):
        del attrs["event_date"]
        del attrs["event_time"]
        return attrs


class SerializersProblemSolve(serializers.ModelSerializer):

    event_id = serializers.IntegerField()
    zabbix_id = serializers.IntegerField()
    zabbix_code = serializers.CharField(max_length=64)
    name = serializers.CharField(max_length=255)
    level = serializers.CharField(max_length=32)
    solve_date = serializers.CharField(max_length=32)
    solve_time = serializers.CharField(max_length=32)

    class Meta:
        model = Problem
        fields = ["event_id", "zabbix_id", "zabbix_code", "name", "level", "solve_date", "solve_time"]

    def validate(self, attrs):
        del attrs["solve_date"]
        del attrs["solve_time"]
        return attrs
