# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: tsTcIntSS.py
@time: 2017/3/2 15:56
SocketServer 客户端
"""
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('>')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()
