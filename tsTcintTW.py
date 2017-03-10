# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: tsTcintTW.py
@time: 2017/3/7 15:46
twisted 客户端
"""
from twisted.internet import protocol, reactor
import struct
from frame_factory import DownProtocol
import json

# HOST = '192.168.0.173'
HOST = 'localhost'
PORT = 21567


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        # frameFactory = DownProtocol()
        # meterAddr = '33304552'
        # result1 = frameFactory.encodeReadFrame(meterAddr, '8010')
        # data = []
        # for j in range(0, len(result1)):
        #     data.append(struct.pack('B', result1[j]))
        data = raw_input('>')
        if data:
            print '...sending %s ...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        # temp = json.load(data)
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection: %s.' % reason.getErrorMessage()
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print 'connection Failed:%s' % reason.getErrorMessage()
        reactor.stop()
        # clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
