# -*- coding: utf-8 -*-
# 模型分类
# 作者: 三石
# 时间: 2022-02-18


import enum
import uuid
from django.utils.html import format_html
from django.db import models
from base.enums import EnumDeviceType


class Classify(models.Model):

    id = models.CharField(primary_key=True, editable=False, default=uuid.uuid4, max_length=64)
    device_type = models.CharField(max_length=32, choices=[(e.name, e.value) for e in EnumDeviceType], verbose_name="设备类型", unique=True)
    name = models.CharField(max_length=32, verbose_name="分类名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    remark = models.TextField(verbose_name="备注", null=True, blank=True)

    def __str__(self):
        return self.name

    # 定义表名称
    class Meta:
        verbose_name = "模型分类"
        verbose_name_plural = verbose_name
