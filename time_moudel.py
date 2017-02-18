# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: time_moudel.py
@time: 2017/2/18 15:30
"""
import time
import datetime
import threading


def takeTask():
    time.sleep(3)
    print "wake up"


startTime = time.time()
for i in range(1, 10):
    product = i * i
    time.sleep(0.1)
    print product
endTime = time.time()
print endTime - startTime

threadObj = threading.Thread(target=takeTask)
threadObj.start()

now = datetime.datetime.now()
print now.year, '-', now.month, '-', now.day
print now.hour, now.minute, now.second
print now.strftime('%Y/%m/%d %H:%M:%S')
