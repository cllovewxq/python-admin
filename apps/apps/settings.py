"""
Django settings for apps project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import logging.config
from pathlib import Path
from .log import LogConfig

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9=ftw!$q!f&a4*qd2si4pyix)llbyq@61%7==bs9k&%k2db7fl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [

    'simpleui',
    'rest_framework',
    'django_apscheduler',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base',
    'host',
    'model',
    'problem',
    'station',
    'zabbix',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'apps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DB_IP = "127.0.0.1"
DB_NAME_DATA = "data"
DB_NAME_ZABBIX = "zabbix"
DB_PORT = "5432"
DB_USERNAME = "postgres"
DB_PASSWORD = "postgres"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME_DATA,
        'HOST': DB_IP,
        'PORT': DB_PORT,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'OPTIONS': {
            'options': '-c search_path=public'
        }

        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    },
    'zabbix': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME_ZABBIX,
        'HOST': DB_IP,
        'PORT': DB_PORT,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'OPTIONS': {
            'options': '-c search_path=public'
        }
    }
}


DATABASE_ROUTERS = [
    'apps.db_router.ZabbixRouter',
]


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URL控制
APPEND_SLASH = False


ZABBIX_IP = "127.0.0.1"
ZABBIX_TOKEN = "857d81b382d352b2808ba9a6ff004eab8c357cc169e46649170ffbed80d81273"


# 日志
# 定义logger
logger = logging.getLogger(__name__)
# 导入配置信息
logging.config.dictConfig(LogConfig)


# simple ui 配置
SIMPLEUI_HOME_INFO = False
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'dynamic': True,
    'menus': [
        {
            'app': 'station',
            'name': '台站模块',
            'icon': 'fas fa-home',
            'models': [
                {
                    'name': '台站管理',
                    'icon': 'fa fa-tag',
                    'url': 'station/station/'
                }
            ]
        },
        {
            'app': 'problem',
            'name': '告警模块',
            'icon': 'fas fa-question',
            'models': [
                {
                    'name': '告警管理',
                    'icon': 'fa fa-tag',
                    'url': 'problem/problem/'
                }
            ]
        },
        {
            'app': 'host',
            'name': '设备模块',
            'icon': 'fas fa-desktop',
            'models': [
                {
                    'name': '交换机',
                    'icon': 'fa fa-tag',
                    'url': 'host/switch/'
                }
            ]
        },
        {
            'app': 'model',
            'name': '模型模块',
            'icon': 'fas fa-archive',
            'models': [
                {
                    'name': '模型分类',
                    'icon': 'fa fa-tag',
                    'url': 'model/classify/'
                },
                {
                    'name': '模型管理',
                    'icon': 'fa fa-tag',
                    'url': 'model/model/'
                }
            ]
        },
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-tag',
                    'url': 'auth/user/'
                }, {
                    'name': '角色',
                    'icon': 'fa fa-tag',
                    'url': 'auth/group/'
                }
            ]
        }
    ]
}