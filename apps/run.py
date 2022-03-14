#!/usr/bin/env python3
# coding: utf-8


import sys
import subprocess


if __name__ == '__main__':
    subprocess.call('python manage.py runserver 0.0.0.0:8000 --noreload --insecure', shell=True,
                    stdin=sys.stdin, stdout=sys.stdout)
