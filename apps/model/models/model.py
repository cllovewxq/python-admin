# -*- coding: utf-8 -*-
# 模型
# 作者: 三石
# 时间: 2022-02-18


import enum
import uuid
from django.utils.html import format_html
from django.db import models
from model.models import Classify
from zabbix.models import Hosts


class Model(models.Model):

    db_templates = Hosts.objects.using("zabbix").filter(status=3).values_list("hostid", "name")

    id = models.CharField(primary_key=True, editable=False, default=uuid.uuid4, max_length=64)
    classify = models.ForeignKey(Classify, on_delete=models.CASCADE, verbose_name="所属模型分类")
    name = models.CharField(max_length=32, verbose_name="模型名称")
    template_id = models.IntegerField(choices=db_templates, verbose_name="模板ID")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    remark = models.TextField(verbose_name="备注", null=True, blank=True)

    def __str__(self):
        return self.name

    # 定义表名称
    class Meta:
        verbose_name = "模型"
        verbose_name_plural = verbose_name
