# -*- coding: utf-8 -*-
# hosts
# 作者: 三石
# 时间: 2021-11-02


from django.db import models


class Hosts(models.Model):

    hostid = models.BigIntegerField(primary_key=True, editable=False)
    host = models.CharField(max_length=128, unique=True)
    status = models.IntegerField(default=0)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    # 定义表名称
    class Meta:
        app_label = "zabbix"
        db_table = "hosts"
