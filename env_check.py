# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: env_check.py
@time: 2017/2/17 14:39
检查系统的环境变量
"""

import os

# 读取系统环境变量
confdir = os.getenv("JAVA_HOME")
conf_file = 'jre\\bin\\server\\Xusage.txt'
# 将conf_file加到confdir
conf_filename = os.path.join(confdir, conf_file)
for env_check in open(conf_filename):
    # env_check = env_check.strip()
    new_env = os.getenv(env_check)
    # print new_env
    if new_env is None:
        print env_check, 'is not set'
print conf_filename