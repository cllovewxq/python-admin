"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views as base_views
from base.views.favicon import favicon_view
from host import views as host_views
from zabbix.views.test import TestAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('favicon.ico', favicon_view, name="favicon视图"),

    path('host/switch/enable/<switch_id>/', host_views.SwitchEnableAPIView.as_view(), name="交换机启用"),
    path('host/switch/disable/<switch_id>/', host_views.SwitchDisableAPIView.as_view(), name="交换机禁用"),

    path('base/', base_views.BaseTemplateView.as_view(), name="基础"),

    path('test/', TestAPIView.as_view(), name="测试"),
]


admin.site.site_header = "台站统一监控平台"
admin.site.site_title = "台站统一监控平台"
