# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: connectiontest.py
@time: 2017/3/9 18:56
@function：twisted 异步请求
"""
from twisted.internet import reactor, defer, protocol
import sys


class CallbackAndDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.deferred.callback("Connected!")
        self.transport.loseConnection()


class ConnectTestFactory(protocol.ClientFactory):
    protocol = CallbackAndDisconnectProtocol

    def __init__(self):
        self.deferred = defer.Deferred()

    def clientConnectionFailed(self, connector, reason):
        self.deferred.errback(reason)


def testConnect(host, port):
    testFactory = ConnectTestFactory()
    reactor.connectTCP(host, port, testFactory)
    return testFactory.deferred


def handleSuccess(result, port):
    print 'connected to port %s' % port
    reactor.stop()


def handleFail(failure, port):
    print 'error to port %s' % port, failure.getErrorMessage()
    reactor.stop()


if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print 'usage:connectiontest.py host port'
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    print sys.argv[1], sys.argv[2]
    # host = 'localhost'
    # port = 21567
    connecting = testConnect(host, port)
    connecting.addCallback(handleSuccess, port)
    connecting.addErrback(handleFail, port)
    reactor.run()
