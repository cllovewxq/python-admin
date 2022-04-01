# -*- coding: utf-8 -*-
# 视图 告警
# 作者: 三石
# 时间: 2022-02-21


import logging
from datetime import datetime
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from base.enums import EnumCode, EnumMsg
from host.api import ApiDevice
from problem.serializers import SerializersProblemCreate, SerializersProblemSolve
from problem.models import Problem
from zabbix.api import ApiEvent


logger = logging.getLogger(__name__)


class ProblemCreateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(data={"code": EnumCode.Success.value})

    def post(self, request):
        logger.debug("Post请求信息: {}".format(request.data))

        serializer = SerializersProblemCreate(data=request.data)
        if serializer.is_valid():
            zabbix_id = serializer.initial_data.get("zabbix_id")
            zabbix_code = serializer.initial_data.get("zabbix_code")
            event_id = serializer.initial_data.get("event_id")
            event_date = serializer.initial_data.get("event_date")
            event_time = serializer.initial_data.get("event_time")

            api = ApiDevice()
            response = api.get(zabbix_id=zabbix_id, zabbix_code=zabbix_code)

            # 过滤告警
            if not response:
                logger.debug("过滤非平台下创建的主机告警")
                return Response(data={"code": EnumCode.Success.value})

            # 拼接触发时间
            trigger_time_str = "{} {}".format(event_date, event_time)
            trigger_time = datetime.strptime(trigger_time_str, "%Y.%m.%d %H:%M:%S")

            serializer.save(device_type=response.get("device_type"), device_id=response.get("device_id"), device_code=response.get("device_code"),
                            trigger_time=trigger_time)

            logger.info("成功接收一条告警: {}".format(event_id))
            return Response(data={"code": EnumCode.Success.value})
        else:
            logger.debug("序列化未通过: {}".format(serializer.errors))
            return Response(data={"code": EnumCode.Success.value})


class ProblemSolveAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(data={"code": EnumCode.Success.value})

    def post(self, request):
        logger.debug("Post请求信息: {}".format(request.data))

        event_id = request.data.get("event_id")
        problem = Problem.objects.filter(event_id=event_id).exists()
        if problem:

            db_problem = Problem.objects.get(event_id=event_id)
            serializer = SerializersProblemSolve(data=request.data, instance=db_problem)

            if serializer.is_valid():
                zabbix_id = serializer.initial_data.get("zabbix_id")
                zabbix_code = serializer.initial_data.get("zabbix_code")

                solve_date = serializer.initial_data.get("solve_date")
                solve_time = serializer.initial_data.get("solve_time")

                api = ApiDevice()
                response = api.get(zabbix_id=zabbix_id, zabbix_code=zabbix_code)

                # 过滤告警
                if not response:
                    logger.debug("过滤非平台下创建的主机告警")
                    return Response(data={"code": EnumCode.Success.value})

                # 拼接解决时间
                solve_time_str = "{} {}".format(solve_date, solve_time)
                solve_time = datetime.strptime(solve_time_str, "%Y.%m.%d %H:%M:%S")

                serializer.save(device_type=response.get("device_type"), device_id=response.get("device_id"), device_code=response.get("device_code"),
                                solve_time=solve_time, status=Problem.StatusChoices.resolved.name)

                logger.info("成功接收一条告警: {}".format(event_id))
                return Response(data={"code": EnumCode.Success.value})
            else:
                logger.debug("序列化未通过: {}".format(serializer.errors))
                return Response(data={"code": EnumCode.Success.value})
        else:
            logger.debug("恢复告警, 原告警数据不存在: {}".format(event_id))
            return Response(data={"code": EnumCode.Success.value})


class ProblemAcknowledgeAPIView(APIView):

    def get(self, request, problem_id, *args, **kwargs):

        problem = Problem.objects.filter(id=problem_id).exists()
        if not problem:
            messages.warning(request, EnumMsg.NotFound.value)
            return redirect("/admin/problem/problem/")

        db_problem = Problem.objects.get(id=problem_id)

        api = ApiEvent()
        api.update_acknowledge(event_id=db_problem.event_id)

        db_problem.ack_status = Problem.AckStatusChoices.yes.name
        db_problem.save(update_fields=["ack_status"])

        messages.success(request, EnumMsg.SuccessEnable.value)
        return redirect("/admin/problem/problem/")

    def post(self, request, *args, **kwargs):
        messages.info(request, EnumMsg.MethodNotSupport.value.format("POST"))
        return redirect("/admin/problem/problem/")
