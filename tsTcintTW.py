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
from frame_factory import UpProtocol
import array
import json

HOST = '219.128.125.98'
# HOST = 'localhost'
PORT = 9800
terminal = '88400036'


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = raw_input('>')
        if data:
            print '...sending %s ...' % data
            print array.array('B', login)
            send_data = json.dumps(array.array('B', login))
            self.transport.write(send_data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print self.upFactory.decodeFrame(data)
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


frameFactory = UpProtocol()
login = frameFactory.frame_login(terminal)
print login
reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
