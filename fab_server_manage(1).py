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
import os
import re
import sys
import smtplib
# import pyzmail

#------------------------------------
# Custom Variables
#------------------------------------
env.hodi_dbg_apk_path      = "/home/linjk/usr/nginx/html/hodi_dbg/hodicloud"
env.upload_apk_server_name = "paytf.apk"

env.roledefs = {
    'source_ctrl': ['root@192.168.0.238'],
    'business_server': ['linjk@192.168.0.193']
}

env.passwords = {
    'root@192.168.0.238:22': "hodi#123",
    'linjk@192.168.0.193:22': 'ljk121'
}

#------------------------------------
# Output All Server's Uptime information
#------------------------------------
@task
@roles('source_ctrl', 'business_server')
def show_uptime():
    run('uptime')

#------------------------------------
# Send a E-mail
#------------------------------------
@task
@roles('business_server')
def send_mail():
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    ehol_result = smtpObj.ehlo()
    print green(ehol_result)
    if int(ehol_result[0]) == 250:
        print yellow("[Info]Connect qq mail server success.")
        try:
            login_result = smtpObj.login('3231047458@qq.com', 'shenzhennuli8')
            print green(login_result)
            if int(login_result[0]) == 235:
                print yellow('[Info]qq mail login success.')
                send_result = smtpObj.sendmail('3231047458@qq.com', 'linjk121@163.com', 'Subject:So long.\n I use Python to send a e-mail to you, haha. Jim')
                if send_result.len() == 0:
                    print green('--- Send mail success.')
                else:
                    print red('[Error]Send mail failed.')
                smtpObj.quit()
        except smtplib.SMTPAuthenticationError as err:
            print "[Error: smtplib.SMTPAuthenticationError]: " + str(err)
            smtpObj.quit()
    else:
        smtpObj.quit()

#------------------------------------
# Upload file to a server 
#------------------------------------
@task
@roles('business_server')
def upload_file_to_server():
    input = prompt("Upload File to which server:\n--1. 192.168.0.193\n--2. 192.168.0.238\n> ")

    if int(input) == 1:
        apk_path = prompt("\nPlease input the apk's path:\n>")
        if apk_path == "":
            print red("APK file cannot empty.")
        else:
            re_result = re.match('^[/\w]+[a-zA-Z0-9].apk$', apk_path)
            if re_result is not None:
                if os.path.exists(apk_path):
                    with cd("/home/linjk/usr"):
                        with settings(warn_only=True):
                            print yellow("Uploading file, please wait...")
                            result = put(apk_path, env.upload_apk_server_name)
                        if result.failed and not confirm("--Upload file failed, Continue[Y/N]?"):
                            abort("--Aborting file upload task.")
                        uploaded_apk = "paytf_%s_.apk" % time.strftime("%Y%m%d")
                        sudo("mv %s %s/%s" % (env.upload_apk_server_name ,env.hodi_dbg_apk_path, uploaded_apk))
                        with cd(env.hodi_dbg_apk_path):
                            sudo("cp %s paytf_hodi.apk" % uploaded_apk)
                            print green("Now you can get the debug apk file from:\"http://192.168.0.193:6607/hodi_dbg/hodicloud/paytf_hodi.apk\"")
                else:
                    print red("Can not find the specified apk file.")
            else:
                print red("Not a valid apk file")

    if int(input) == 2:
        print red("--You can not upload file to this server now.")


