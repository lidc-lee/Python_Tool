# coding=utf-8

"""

@version: ??
@author: AA-ldc
@file: tsTcIntSS.py
@time: 2017/3/2 15:56
SocketServer 客户端
"""
from socket import *
from frame_factory import UpProtocol
import array

HOST = '219.128.125.98'
PORT = 9800
BUFSIZE = 2048
ADDR = (HOST, PORT)
meterAddr = '88400036'

def getData():
    all_data = []
    all_data.append(array.array('B', frameFactory.frame_login(meterAddr)))
    all_data.append(array.array('B', frameFactory.frame_connection(meterAddr)))
    return all_data

frameFactory = UpProtocol()
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
request_data = getData()
tcpCliSock.send(request_data[0])
back_data = tcpCliSock.recv(BUFSIZE)
result = frameFactory.decodeFrame(back_data)
print result[0], '---', result[3]
request_data = request_data[1:]
if result[3] == '登录返回正常':
    print request_data
    tcpCliSock.send(request_data[0])
    back_data = tcpCliSock.recv(BUFSIZE)
    result = frameFactory.decodeFrame(back_data)
    print result[0], '---', result[3]
tcpCliSock.close()
