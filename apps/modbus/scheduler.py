# -*- coding: utf-8 -*-
# 任务调度
# 作者: 三石
# 时间: 2022-02-07


import logging
from datetime import datetime
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from multiprocessing import cpu_count
from modbus.jobs import read as jobs_read


logger = logging.getLogger(__name__)


def init_scheduler() -> BackgroundScheduler:
    """
    初始化任务调度
    :return:
    """

    logger.info("================================================================================================")
    logger.info("初始化任务调度")

    # 线程池
    executors = {
        "default": ThreadPoolExecutor(30),
        "processpool": ProcessPoolExecutor(cpu_count()),
    }

    # 任务配置
    job_defaults = {
        'coalesce': False,
        'max_instances': 5,
        'misfire_grace_time': 10  # 10秒的任务超时容错
    }

    # 后台定时任务
    scheduler = BackgroundScheduler(timezone="Asia/Shanghai", executors=executors, job_defaults=job_defaults)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Modbus服务任务
    scheduler.add_job(
        jobs_read.job_modbus_read_demo,
        id="job_modbus_read_demo",
        # trigger="date",
        # next_run_time=datetime.now(),
        trigger="cron",
        second=0,
        replace_existing=True,
        kwargs={
            "devices": [
                {
                    "code": "napro",
                    "ipaddress": "172.16.3.66",
                    "port": 502
                }
            ]
        }
    )

    return scheduler
