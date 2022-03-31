# -*- coding: utf-8 -*-
# 发射机
# 作者: 三石
# 时间: 2022-02-07


from django.db import models


class Transmitter(models.Model):

    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)
