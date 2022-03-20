# -*- coding: utf-8 -*-
# 视图 授权
# 作者: 三石
# 时间: 2022-02-21


import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


logger = logging.getLogger(__name__)


class BaseTemplateView(APIView):

    template_name = 'base.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        logger.info("Get请求信息: {}".format(request.query_params))

        return Response(data={"code": 10000})
