# Generated by Django 4.0.3 on 2022-03-31 16:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('device_type', models.CharField(choices=[('switch', '交换机')], max_length=32, verbose_name='设备类型')),
                ('device_id', models.IntegerField(verbose_name='设备ID')),
                ('device_code', models.CharField(max_length=32, verbose_name='设备编号')),
                ('zabbix_id', models.BigIntegerField(verbose_name='Zabbix ID')),
                ('zabbix_code', models.CharField(max_length=64, verbose_name='zabbix 编号')),
                ('event_id', models.BigIntegerField(verbose_name='事件ID')),
                ('name', models.CharField(max_length=255, verbose_name='告警名称')),
                ('ack_status', models.CharField(choices=[('no', '未确认'), ('yes', '已确认')], default='no', max_length=32, verbose_name='确认状态')),
                ('status', models.CharField(choices=[('pending', '待处理'), ('resolved', '已解决')], default='pending', max_length=32, verbose_name='状态')),
                ('level', models.CharField(max_length=32, verbose_name='级别')),
                ('trigger_time', models.DateTimeField(verbose_name='触发时间')),
                ('solve_time', models.DateTimeField(null=True, verbose_name='解决时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '告警',
                'verbose_name_plural': '告警',
            },
        ),
    ]
