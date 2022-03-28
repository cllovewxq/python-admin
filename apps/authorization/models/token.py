# -*- coding: utf-8 -*-
# token
# 作者: 三石
# 时间: 2022-02-07


import enum
import uuid
from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User


class Token(models.Model):

    id = models.CharField(primary_key=True, editable=False, default=uuid.uuid4, max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")
    token = models.TextField(verbose_name="API Token")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    remark = models.TextField(verbose_name="备注", null=True, blank=True)

    def __str__(self):
        return str(self.id)

    # 定义表名称
    class Meta:
        verbose_name = "Token"
        verbose_name_plural = verbose_name
