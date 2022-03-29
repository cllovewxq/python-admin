# Generated by Django 4.0.3 on 2022-03-29 10:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('host_group', models.UUIDField(default=uuid.UUID('72b1f6bf-63ad-4b93-a409-914268732ecf'), verbose_name='主机组编号')),
                ('host_group_id', models.CharField(max_length=32, verbose_name='主机组ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '台站',
                'verbose_name_plural': '台站',
            },
        ),
    ]
