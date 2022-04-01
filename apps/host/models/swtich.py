# -*- coding: utf-8 -*-
# 交换机
# 作者: 三石
# 时间: 2022-02-07


import enum
import uuid
from django.db import models
from django.utils.html import format_html
from django.core.validators import MinValueValidator, MaxValueValidator
from station.models import Station
from model.models import Model


class Switch(models.Model):

    Prefix = "SW-{}"
    DeviceType = ""

    class StatusChoices(enum.Enum):
        """状态"""

        enable = "启用"
        disable = "禁用"

    id = models.AutoField(primary_key=True, editable=False)
    code = models.CharField(max_length=32, verbose_name="设备编号")
    station = models.ForeignKey(Station, on_delete=models.CASCADE, verbose_name="所属台站")
    zabbix_id = models.BigIntegerField(verbose_name="Zabbix ID")
    zabbix_code = models.CharField(max_length=64, verbose_name="zabbix 编号", default=uuid.uuid4)
    name = models.CharField(max_length=32, verbose_name="设备名称", unique=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name="所属模型")
    ipaddress = models.CharField(max_length=32, verbose_name="设备IP")
    port = models.IntegerField(verbose_name="设备端口", validators=[MinValueValidator(1), MaxValueValidator(65536)], default=161)
    snmp_community = models.CharField(max_length=64, verbose_name="SNMP共同体名")
    status = models.CharField(max_length=16, choices=[(e.name, e.value) for e in StatusChoices], verbose_name="状态", default=StatusChoices.enable.name)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    remark = models.TextField(verbose_name="备注", null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def status_operation(self):
        value = self.StatusChoices[str(self.status)].value
        if self.status == self.StatusChoices.enable.name:
            return format_html('<a href="/host/switch/disable/{id}/"><font color="#009100">{value}</a>'.format(id=self.id, value=value))
        elif self.status == self.StatusChoices.disable.name:
            return format_html('<a href="/host/switch/enable/{id}/"><font color="#FF0000">{value}</a>'.format(id=self.id, value=value))

        return value

    status_operation.short_description = "状态"

    def operation(self):
        return format_html('<a href="/history/{host_id}/get/">[最新数据]</a>&nbsp;&nbsp;'
                           '<a href="/admin/problem/problem/?device_code={code}" target="_blank">[告警]</a>&nbsp;&nbsp;'.format(host_id=self.id, code=self.code))

    operation.short_description = "操作"

    # 定义表名称
    class Meta:
        verbose_name = "交换机"
        verbose_name_plural = verbose_name
