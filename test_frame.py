# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: test_frame.py
@time: 2017/3/6 18:54

"""
from frame_factory import DownProtocol
from frame_factory import UpProtocol
import struct

if __name__ == '__main__':

    frameFactory = DownProtocol()
    meterAddr = '33304552'
    result1 = frameFactory.encodeReadFrame(meterAddr, '8010')
    data = ['02', 'AA', 'AA', 'DB', '80', '7D', '62', '26', '49']
    result2 = frameFactory.encodeWriteFrame(meterAddr, data, 9, '8010')
    print result1
    # print result2
    hexStr = ''
    for i in range(0, len(result2)):
        hexStr += hex(result2[i])
    # print hexStr.upper().split('0X')
    array = []
    result3 = ['68', '76', '45', '30', '33', '16', '52', '68', '81', '0B', '43', 'B3', '81', '25', '9B', '07', '27',
               '3B', 'DD', 'DD', '35', '71', '16']
    result4 = []
    for i in range(0, len(result3)):
        result4.append(int(result3[i], 16))
        array.append(struct.pack('B', result4[i]))
    value = frameFactory.decodeFrame(array)
    print value[0] + "---" + value[1] + "---" + value[3]

    protocol_server = UpProtocol()
    login = protocol_server.frame_login(meterAddr)
    print '登陆通信服务器帧---', login
    connect = protocol_server.frame_connection(meterAddr)
    print '连接通信服务器帧---', connect
    disconnect = protocol_server.frame_disconnection(meterAddr)
    print '断开连接通信服务器帧---', disconnect
    logout = protocol_server.frame_logout(meterAddr)
    print '登出通信服务器帧---', logout
    read = protocol_server.frame_read_data(meterAddr, '8010')
    print '读数据--', read
    write = protocol_server.frame_write_data(meterAddr, '8010', 0x0B, data)
    print '写数据--', write
    real_time = protocol_server.frame_real_time(meterAddr, '152533304552', 0x02, '9010')
    print '实时抄--', real_time
    server = ['68', '80', '00', '01', '00', 'A0', '00', '68', '81', '13', '00', '01', '00', '00', '00', '00',
              '00', '00', '00', '10', '80', '49', '26', '62', '7D', '80', 'DB', 'AA', 'AA', '02', '15', '16']
    array_server = []
    for i in range(0, len(server)):
        array_server.append(struct.pack('B', int(server[i], 16)))
    value2 = protocol_server.decodeFrame(array_server)
    print '解帧--', value2