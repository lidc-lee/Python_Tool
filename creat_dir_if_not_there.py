# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: creat_dir_if_not_there.py
@time: 2017/2/17 14:27
如果不存在则创建目录
"""

import os

try:
    home = os.path.expanduser("~")
    print home

    if not os.path.exists(home + '/testdir'):
        os.makedirs(home + "/testdir")

    if not os.path.exists('testdir'):
        os.makedirs('testdir')
except Exception, e:
    print e
