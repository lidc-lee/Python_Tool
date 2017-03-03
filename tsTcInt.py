# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: tsTcInt.py
@time: 2017/2/24 19:09
TCP客户端
"""
from socket import *

HOST = '127.0.0.1'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpCliSock.close()
