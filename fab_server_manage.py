#!/usr/bin/env python
# coding=utf-8
# Usage: fab -f fab_server_manage.py <your_task_name>
# By:   linjk
# Date: 2017/01/13
# 上传文件到服务器

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
import time

# ------------------------------------
# Custom Variables
# ------------------------------------
env.hodi_dbg_apk_path = "/home/linjk/usr/nginx/html/hodi_dbg/hodicloud"

env.roledefs = {
    'source_ctrl': ['root@192.168.0.238'],
    'business_server': ['linjk@192.168.0.193']
}

env.passwords = {
    'root@192.168.0.238:22': "hodi#123",
    'linjk@192.168.0.193:22': 'ljk121'
}


# ------------------------------------
# 查看每台服务器的启动时间
# ------------------------------------
@task
@roles('source_ctrl', 'business_server')
def show_uptime():
    run('uptime')


# ------------------------------------
# 上传文件到指定服务器 
# ------------------------------------
@task
@roles('business_server')
def upload_file_to_server():
    input = prompt("Upload File to which server:\n--1. 192.168.0.193\n--2. 192.168.0.238\n> ")
    if int(input) == 1:
        with cd("/home/linjk/usr"):
            with settings(warn_only=True):
                print yellow("Uploading file, please wait...")
                result = put("C:/Users/AA/Desktop/paytf2.0.1609080.apk", "paytf.apk")
                uploaded_apk = "paytf_%s_.apk" % time.strftime("%Y%m%d")
                sudo("mv paytf.apk %s/%s" % (env.hodi_dbg_apk_path, uploaded_apk))
                with cd(env.hodi_dbg_apk_path):
                    sudo("cp %s paytf_hodi.apk" % uploaded_apk)
            if result.failed and not confirm("--Upload file failed, Continue[Y/N]?"):
                abort("--Aborting file upload task.")
    if int(input) == 2:
        print red("--You can not upload file to this server now.")
