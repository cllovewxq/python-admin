# -*- coding: utf-8 -*-
# app与数据库映射关系类
# 作者: 三石
# 时间: 2020-08-28


class ZabbixRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'zabbix':
            return 'zabbix'
        else:
            return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'zabbix':
            return 'zabbix'
        else:
            return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'zabbix':
            return db == 'zabbix'
        else:
            return None
