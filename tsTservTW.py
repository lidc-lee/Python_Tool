# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: tsTservTW.py
@time: 2017/3/7 15:31
twisted 框架的tcp服务器
"""
from twisted.internet import protocol, reactor
from time import ctime
import json
PORT = 21567


class TSServProtocol(protocol.Protocol):
    # 重写
    def connectionMade(self):
        host = self.transport.getPeer().host
        print 'conected from :', host

    def dataReceived(self, data):
        # temp = json.load(data)
        self.transport.write('于[%s] %s收到' % (ctime(), data))


factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()
