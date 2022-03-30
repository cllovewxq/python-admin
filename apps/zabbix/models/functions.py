# -*- coding: utf-8 -*-
# function
# 作者: 三石
# 时间: 2021-11-02


import enum
from django.db import models


class Functions(models.Model):

    functionid = models.BigIntegerField(primary_key=True, editable=False)
    itemid = models.IntegerField()
    triggerid = models.IntegerField()
    name = models.CharField(max_length=12)
    parameter = models.CharField(max_length=255)

    def __str__(self):
        return self.functionid

    # 定义表名称
    class Meta:
        app_label = "zabbix"
        db_table = "functions"
