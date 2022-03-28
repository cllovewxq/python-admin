# -*- coding: utf-8 -*-
# admin 课程
# 作者: 三石
# 时间: 2022-02-15


from django.contrib import admin
from authorization.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'create_time', )
    ordering = ('-create_time', )
    list_per_page = 20
    search_fields = ('user', )
