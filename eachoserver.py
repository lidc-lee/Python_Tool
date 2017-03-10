# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: eachoserver.py
@time: 2017/3/10 10:05
@function：accepting connections from clients
"""
from twisted.internet import reactor, protocol
from twisted.protocols import basic

PORT = 55555


class EchoProtocol(basic.LineReceiver):
    def connectionMade(self):
        host = self.transport.getPeer().host
        print 'conected from :', host

    def lineReceived(self, line):
        if line == 'quit':
            self.sendLine('Goodbye')
            self.transport.loseConnection()
        else:
            self.sendLine('You said:' + line)


class EchoServerFactory(protocol.ServerFactory):
    protocol = EchoProtocol


if __name__ == '__main__':
    print 'waiting for connection...'
    reactor.listenTCP(PORT, EchoServerFactory())
    reactor.run()
