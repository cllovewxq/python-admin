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
from history import views as history_views
from host import views as host_views
from problem import views as problem_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('favicon.ico', favicon_view, name="favicon视图"),

    path('host/switch/enable/<switch_id>/', host_views.SwitchEnableAPIView.as_view(), name="交换机启用"),
    path('host/switch/disable/<switch_id>/', host_views.SwitchDisableAPIView.as_view(), name="交换机禁用"),

    path('problem/problem/acknowledge/<problem_id>/', problem_views.ProblemAcknowledgeAPIView.as_view(), name="告警确认"),

    path('history/<host_id>/get/', history_views.HistoryHTMLView.as_view(), name="历史"),
    path('api/problem/create/', problem_views.ProblemCreateAPIView.as_view(), name="告警创建"),
    path('api/problem/solve/', problem_views.ProblemSolveAPIView.as_view(), name="告警解决"),

    path('base/', base_views.BaseTemplateView.as_view(), name="基础"),
]


admin.site.site_header = "台站统一监控平台"
admin.site.site_title = "台站统一监控平台"
