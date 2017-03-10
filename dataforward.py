# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: dataforward.py
@time: 2017/3/10 9:29
@function：twisted 发送和接收数据
"""
import re
import sys

from twisted.internet import reactor, protocol
from twisted.internet import stdio


class DataForwardingProtocol(protocol.Protocol):
    def __init__(self):
        self.output = None
        self.normalizeNewlines = False

    def dataReceived(self, data):
        if self.normalizeNewlines:
            data = re.sub(r"(\r\n|\n)", "\r\n", data)
        if self.output:
            self.output.write(data)


class StdioProxyProtocol(DataForwardingProtocol):
    def connectionMade(self):
        intputForwarder = DataForwardingProtocol()
        intputForwarder.output = self.transport
        intputForwarder.normalizeNewlines = True
        self.output = stdio.StandardIO(intputForwarder)
        print 'connected to server.ctrl-C to close connection'


class StdioProxyFactory(protocol.ClientFactory):
    protocol = StdioProxyProtocol

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection: %s.' % reason.getErrorMessage()
        # reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print reason.gettErrorMessage()
        reactor.stop()


if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print 'usage: %s host port' % __file__
        sys.exit(1)
    reactor.connectTCP(sys.argv[1], int(sys.argv[2]), StdioProxyFactory())
    reactor.run()
