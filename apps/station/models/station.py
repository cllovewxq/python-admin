# -*- coding: utf-8 -*-
# 台站
# 作者: 三石
# 时间: 2022-02-07


import enum
import uuid
from django.db import models
from django.utils.html import format_html


class Station(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    host_group = models.UUIDField(default=uuid.uuid4, verbose_name="主机组编号")
    host_group_id = models.CharField(max_length=32, verbose_name="主机组ID")
    name = models.CharField(max_length=32, verbose_name="名称", unique=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    remark = models.TextField(verbose_name="备注", null=True, blank=True)

    def __str__(self):
        return str(self.name)

    # 定义表名称
    class Meta:
        verbose_name = "台站"
        verbose_name_plural = verbose_name
