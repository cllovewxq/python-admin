# -*- coding: utf-8 -*-
# 告警
# 作者: 三石
# 时间: 2022-02-07


import enum
import uuid
from django.db import models
from django.utils.html import format_html
from base.enums import EnumDeviceType
from host.api import ApiDevice


class Problem(models.Model):

    class AckStatusChoices(enum.Enum):
        """确认状态"""

        no = "未确认"
        yes = "已确认"

    class StatusChoices(enum.Enum):
        """状态"""

        pending = "待处理"
        resolved = "已解决"

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    device_type = models.CharField(max_length=32, choices=[(e.name, e.value) for e in EnumDeviceType], verbose_name="设备类型")
    device_id = models.IntegerField(verbose_name="设备ID")
    device_code = models.CharField(max_length=32, verbose_name="设备编号")
    zabbix_id = models.BigIntegerField(verbose_name="Zabbix ID")
    zabbix_code = models.CharField(max_length=64, verbose_name="zabbix 编号")
    event_id = models.BigIntegerField(verbose_name="事件ID")
    name = models.CharField(max_length=255, verbose_name="告警名称")
    ack_status = models.CharField(max_length=32, choices=[(e.name, e.value) for e in AckStatusChoices], verbose_name="确认状态", default=AckStatusChoices.no.name)
    status = models.CharField(max_length=32, choices=[(e.name, e.value) for e in StatusChoices], verbose_name="状态", default=StatusChoices.pending.name)
    level = models.CharField(max_length=32, verbose_name="级别")
    trigger_time = models.DateTimeField(verbose_name="触发时间")
    solve_time = models.DateTimeField(verbose_name="解决时间", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    remark = models.TextField(verbose_name="备注", null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def device_name(self):
        name = ApiDevice().get_name_from_type(device_type=self.device_type, zabbix_id=self.zabbix_id, zabbix_code=self.zabbix_code)
        if not name:
            return "设备已被删除"
        else:
            return name

    device_name.short_description = "设备名称"

    def ack_status_operation(self):
        value = self.AckStatusChoices[str(self.ack_status)].value
        if self.ack_status == self.AckStatusChoices.no.name:
            return format_html('<a href="/problem/problem/acknowledge/{id}/"><font color="#0080FF">{value}</a>'.format(id=self.id, value=value))
        return value

    ack_status_operation.short_description = "确认状态"

    def status_value(self):
        if self.status == Problem.StatusChoices.pending.name:
            return format_html('<font color="#FF0000">{value}'.format(value=Problem.StatusChoices.pending.value))
        elif self.status == Problem.StatusChoices.resolved.name:
            return format_html('<font color="#009100">{value}</a>'.format(value=Problem.StatusChoices.resolved.value))

        return "--"

    status_value.short_description = "告警状态"

    # 定义表名称
    class Meta:
        verbose_name = "告警"
        verbose_name_plural = verbose_name
