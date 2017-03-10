# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: calllater.py
@time: 2017/3/9 18:03
@function：twisted
"""
from twisted.internet import reactor
from time import ctime


def printTime():
    print 'current time is ', ctime()

def stopReactor():
    print 'stoping reactor'
    reactor.stop()

reactor.callLater(1, printTime)
reactor.callLater(2, printTime)
reactor.callLater(3, printTime)
reactor.callLater(4, printTime)
reactor.callLater(5, printTime)
reactor.callLater(6, stopReactor)

print 'running the reactor...'
reactor.run()
print 'reactor stopped'

