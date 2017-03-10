# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: myThread.py
@time: 2017/3/9 15:50
@function：Thread子类
"""
import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def getResult(self):
        return self.res

    def run(self):
        print 'starting', self.name, 'at:', ctime()
        self.res = self.func(*self.args)
        print self.name, 'finished at:', ctime()
