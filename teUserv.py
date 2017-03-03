# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: teUserv.py
@time: 2017/3/2 15:35
udp服务器
"""
from socket import *
from time import ctime

HOST = ''
POST = 21567
BUFSIZ = 1024
ADDR = (HOST, POST)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
    print "waiting for massage..."
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print "...received from and returned to :", addr

udpSerSock.close()
