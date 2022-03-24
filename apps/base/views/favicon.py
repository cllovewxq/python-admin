# -*- coding: utf-8 -*-
# 视图 favicon
# 作者: 三石
# 时间: 2021-11-04


import os
from django.http import HttpResponse
from django.conf import settings


def favicon_view(request):
    """显示favicon"""
    base_path = settings.BASE_DIR
    logo_file = os.path.join(base_path, "static/images/favicon.ico")
    file_favicon = open(logo_file, "rb")
    return HttpResponse(file_favicon.read(), content_type='image/jpg')
