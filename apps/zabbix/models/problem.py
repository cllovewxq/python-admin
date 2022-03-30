# -*- coding: utf-8 -*-
# function
# 作者: 三石
# 时间: 2021-11-02


import enum
from base.utils import UtilsConvert
from django.db import models
from .functions import Functions
from .items import Items
from .hosts import Hosts


class Problem(models.Model):

    eventid = models.BigIntegerField(primary_key=True, editable=False)
    source = models.IntegerField(default=0)
    object = models.IntegerField(default=0)
    objectid = models.BigIntegerField(default=0)
    clock = models.IntegerField(default=0)
    ns = models.IntegerField(default=0)
    r_eventid = models.BigIntegerField(null=True)
    r_clock = models.IntegerField(default=0)
    r_ns = models.IntegerField(default=0)
    correlationid = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=2048)
    acknowledged = models.IntegerField(default=0)
    severity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.eventid)

    def create_time(self):
        return UtilsConvert().get_date_from_timestamp(timestamp=self.clock)

    create_time.short_description = "触发时间"
    create_time.admin_order_field = "-clock"

    def host_name(self):
        db_function = Functions.objects.get(triggerid=self.objectid)
        db_item = Items.objects.get(itemid=db_function.itemid)
        db_host = Hosts.objects.get(hostid=db_item.hostid)
        return db_host.name

    host_name.short_description = "告警对象"

    # 定义表名称
    class Meta:
        app_label = "zabbix"
        db_table = "problem"
