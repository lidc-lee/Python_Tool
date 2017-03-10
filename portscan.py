# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: portscan.py
@time: 2017/3/10 9:09
@function：DeferredList
"""
from twisted.internet import reactor, defer
from connectiontest import testConnect
import sys

def handleAllResults(results, ports):
    for port, resultInfo in zip(ports, results):
        success, result = resultInfo
        # print success
        if success:
            print 'connected to port %i' % port
    reactor.stop()


host = sys.argv[1]
ports = range(1, 201)
testers = [testConnect(host, port) for port in ports]
defer.DeferredList(testers, consumeErrors=True).addCallback(handleAllResults, ports)
reactor.run()
