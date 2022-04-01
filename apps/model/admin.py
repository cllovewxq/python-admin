# -*- coding: utf-8 -*-
# admin
# 作者: 三石
# 时间: 2022-02-15


from django.contrib import admin, messages
from model.models import Classify, Model


@admin.register(Classify)
class ClassifyAdmin(admin.ModelAdmin):

    list_display = ('name', 'device_type', 'create_time', )
    ordering = ('-create_time', )
    list_per_page = 20


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):

    list_display = ('name', 'classify', 'template_id', 'create_time', )
    ordering = ('-create_time', )
    list_per_page = 20
    list_filter = ['classify__name', ]
    search_fields = ('name', 'code', )
