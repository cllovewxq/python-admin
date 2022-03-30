# -*- coding: utf-8 -*-
# itmes
# 作者: 三石
# 时间: 2021-11-02


import enum
from django.db import models


class Items(models.Model):

    class ValueTypeChoices(enum.Enum):
        """值类型"""

        float = 0
        char = 1
        log = 2
        integer = 3
        text = 4

    itemid = models.BigIntegerField(primary_key=True, editable=False)
    type = models.IntegerField()
    hostid = models.IntegerField()
    name = models.CharField(max_length=255)
    value_type = models.IntegerField()

    def __str__(self):
        return self.itemid

    # 定义表名称
    class Meta:
        app_label = "zabbix"
        db_table = "items"
