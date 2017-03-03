# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: tsTserv.py
@time: 2017/2/24 18:54
TCP服务端
"""

from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
# 将主机名和端口号绑定到套接字上
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    # 被动接收客户端连接
    tcpCliSock, addr = tcpSerSock.accept()
    print 'connected form ', addr
    while True:
        # 接收消息
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))
    tcpCliSock.close()

tcpSerSock.close()
