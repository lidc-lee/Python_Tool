# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: frame_factory.py
@time: 2017/3/1 19:15
协议帧工厂方法模式
"""

import struct
from copy import *


# 简单工厂
class DownProtocolFather():
    def __init__(self):
        pass

    # 读数据的组帧方法
    def encodeReadFrame(self, meterAddress, di):
        pass

    # 读后续数据的组帧方法
    def encodeLaterReadFrame(self, meterAddress, di):
        pass

    # 重读
    def encodeReReadFrame(self, meterAddress):
        pass

    # 写数据
    def encodeWriteFrame(self, meterAddress, data, length, di):
        pass

    # 解帧
    def decodeFrame(self, data):
        pass


# 下行协议
class DownProtocol(DownProtocolFather):
    # 构造方法
    def __init__(self):
        print "构造方法"

    # 读数据的组帧方法
    def encodeReadFrame(self, meterAddress, di):
        print '读数据帧'
        temp = copy(meterAddress)
        result = []
        result.append(0xFE)
        result.append(0xFE)
        result.append(0x68)
        while temp:
            result.append(int(temp[len(temp) - 2:], 16))
            temp = temp[:len(temp) - 2]
        result.append(0x68)
        result.append(0x01)
        result.append(0x02)
        while di:
            result.append(int(di[len(di) - 2:], 16) + 0x33)
            di = di[:len(di) - 2]
        cs = getCS(result[2:])
        result.append(cs)
        result.append(0x16)
        return result

    # 读后续数据的组帧方法
    def encodeLaterReadFrame(self, meterAddress, di):
        print '读后数据帧'
        temp = copy(meterAddress)
        result = []
        result.append(0xFE)
        result.append(0xFE)
        result.append(0x68)
        while temp:
            result.append(int(temp[len(temp) - 2:], 16))
            temp = temp[:len(temp) - 2]
        result.append(0x68)
        result.append(0x02)
        result.append(0x02)
        while di:
            result.append(int(di[len(di) - 2:], 16) + 0x33)
            di = di[:len(di) - 2]
        cs = getCS(result[2:])
        result.append(cs)
        result.append(0x16)
        return result

    # 重读
    def encodeReReadFrame(self, meterAddress):
        print '重读数据帧'
        temp = copy(meterAddress)
        result = []
        result.append(0xFE)
        result.append(0xFE)
        result.append(0x68)
        while temp:
            result.append(int(temp[len(temp) - 2:], 16))
            temp = temp[:len(temp) - 2]
        result.append(0x68)
        result.append(0x03)
        result.append(0x00)
        cs = getCS(result[2:])
        result.append(cs)
        result.append(0x16)
        return result

    # 写数据
    def encodeWriteFrame(self, meterAddress, data, length, di):
        print '写数据帧'
        if len(meterAddress) < 12:
            temp = copy('A' * (12 - len(meterAddress)) + meterAddress)
        result = []
        result.append(0xFE)
        result.append(0xFE)
        result.append(0x68)
        while temp:
            result.append(int(temp[len(temp) - 2:], 16))
            temp = temp[:len(temp) - 2]
        result.append(0x68)
        result.append(0x04)
        length += 6
        result.append(length)
        while di:
            result.append(int(di[len(di) - 2:], 16) + 0x33)
            di = di[:len(di) - 2]
        result.append(0x33)
        result.append(0x33)
        result.append(0x33)
        result.append(0x33)
        while data:
            a = int(data[-1], 16) + 0x33
            if a > 255:
                a -= 0x100
            result.append(a)
            data = data[:-1]
        cs = getCS(result[2:])
        result.append(cs)
        result.append(0x16)
        return result

    # 解帧
    def decodeFrame(self, data):
        # 保存数据，包含0--地址，1--数据标识，2--数据项，3--描述信息
        itemvalue = []
        array = []
        index = 0
        for i in range(0, len(data)):
            array.append(struct.unpack('B', data[i])[0])
        print "解帧数据---",array

        while index < len(array):
            if array[index] == 0xFE:
                index += 1
                break
            if array[index] == 0x68:
                index += 1
                # 表号
                MeterAddr = decodeMeterAddr(array[index:index + 6])
                # print MeterAddr
                itemvalue.append(MeterAddr)
                index += 6
                if array[index] == 0x68:
                    index += 1
                    contrlWorld = array[index]
                    # print hex(contrlWorld)
                    # 读数据返回正常
                    if contrlWorld == 0x81 or contrlWorld == 0x82 or contrlWorld == 0xA2 or contrlWorld == 0x83 or contrlWorld == 0xA3:
                        index += 1
                        # 数据域的长度
                        length = array[index]
                        # print length
                        index += 1
                        # 数据区域
                        dataBuf = removeOffset(array[index:index + length])
                        # print dataBuf
                        realData = []
                        for j in range(len(dataBuf) - 1, -1, -1):
                            realData.append(dataBuf[j])
                        # print realData
                        # 数据标识
                        di = realData[-2:]
                        # print di
                        diKey = InterToHex(di)
                        # print str(diKey)
                        # 数据项
                        value = realData[:-2]
                        # print value
                        itemvalue.append(diKey)
                        itemvalue.append(value)
                        itemvalue.append('读数据返回正常')
                        return itemvalue

                    # 读数据返回异常
                    elif contrlWorld == 0xC1 or contrlWorld == 0xC2 or contrlWorld == 0xC3:
                        index += 1
                        length = array[index]
                        index += 1
                        itemvalue.append('')
                        itemvalue.append(array[index:index + length])
                        itemvalue.append('读数据返回异常')
                        return itemvalue
                    elif contrlWorld == 0x84:
                        index += 1
                        length = array[index]
                        print length
                        itemvalue.append('')
                        itemvalue.append('')
                        itemvalue.append('写数据成功')
                        return itemvalue
                    elif contrlWorld == 0xC4:
                        index += 1
                        length = array[index]
                        index += 1
                        itemvalue.append('')
                        itemvalue.append(array[index:index + length])
                        itemvalue.append('写数据异常')
                        return itemvalue


class UpProtocolFather():
    def __int__(self):
        pass

    # 登录通信服务器
    def frame_login(self, terminal):
        pass

    # 连接通信服务器
    def frame_connection(self, terminal):
        pass

    # 断开连接
    def frame_disconnection(self, terminal):
        pass

    # 登出通信服务器
    def frame_logout(self, terminal):
        pass

    # 读数据帧
    def frame_read_data(self, terminal, di):
        pass

    # 写数据帧
    def frame_write_data(self, terminal, di, length, data):
        pass

    # 实时召测命令
    def frame_real_time(self, terminal, meterAddress, seqNo, di):
        pass

    def decodeFrame(self, data):
        pass


# 上行协议
class UpProtocol(UpProtocolFather):
    def __init__(self):
        print '与通信服务器通信构造函数'

    cnt = 0

    # 登录通信服务器
    def frame_login(self, terminal):
        result = self.frame_top(terminal, 0xA0)
        result.append(0x68)
        result.append(0xA1)
        result.append(0x03)
        result.append(0x00)
        result.append(0x11)
        result.append(0x11)
        result.append(0x11)
        cs = getCS(result)
        result.append(cs)
        result.append(0x16)
        return result

    # 连接通信服务器
    def frame_connection(self, terminal):
        result = []
        result.append(0x68)
        result.append(0x88)
        result.append(0x00)
        result.append(0x20)
        result.append(0x00)
        result.append(0x20)
        if self.cnt < 15:
            result.append(self.cnt)
            self.cnt += 1
        else:
            self.cnt = 0
        result.append(0x68)
        result.append(0x25)
        result.append(0x0D)
        result.append(0x00)
        result.append(0x01)
        temp = copy(terminal)
        while temp:
            result.append(int(temp[:2], 16))
            temp = temp[2:]
        for j in range(0, 8):
            result.append(0xFF)
        cs = getCS(result)
        result.append(cs)
        result.append(0x16)
        return result

    # 断开连接
    def frame_disconnection(self, terminal):
        result = self.frame_top(terminal, 0x20)
        result.append(0x68)
        result.append(0x26)
        result.append(0x00)
        result.append(0x00)
        cs = getCS(result)
        result.append(cs)
        result.append(0x16)
        return result

    # 登出通信服务器
    def frame_logout(self, terminal):
        result = self.frame_top(terminal, 0x60)
        result.append(0x68)
        result.append(0xA2)
        result.append(0x00)
        result.append(0x00)
        cs = getCS(result)
        result.append(cs)
        result.append(0x16)
        return result

    # 读数据帧
    def frame_read_data(self, terminal, di):
        result = self.frame_top(terminal, 0xA0)
        result.append(0x68)
        result.append(0x01)
        # 长度
        result.append(0x0A)
        result.append(0x00)
        # 测量点号
        result.append(0x01)
        result.append(0x00)
        result.append(0x00)
        result.append(0x00)
        result.append(0x00)
        result.append(0x00)
        result.append(0x00)
        result.append(0x00)
        while di:
            result.append(int(di[-2:], 16))
            di = di[:-2]
        cs = getCS(result)
        result.append(cs)
        result.append(0x16)
        return result

    # 写数据帧
    def frame_write_data(self, terminal, di, length, data):
        result = self.frame_top(terminal, 0xA0)
        result.append(0x68)
        result.append(0x08)
        length += 8
        # 长度
        result.append(length)
        result.append(0x00)
        # 测量点号
        result.append(0x00)
        result.append(0x00)
        # 权限等级
        result.append(0x11)
        # 密码
        result.append(0x00)
        result.append(0x00)
        result.append(0x00)

        while di:
            result.append(int(di[-2:], 16))
            di = di[:-2]
        while data:
            result.append(int(data[-1], 16))
            data = data[:-1]
        cs = getCS(result)
        result.append(cs)
        result.append(0x16)
        return result

    # 实时召测命令
    def frame_real_time(self, terminal, meterAddress, seqNo, di):
        result = self.frame_top(terminal, 0x60)
        result.append(0x68)
        result.append(0x11)
        result.append(0x23)
        result.append(0x00)

        while meterAddress:
            result.append(int(meterAddress[-2:], 16))
            meterAddress = meterAddress[:-2]
        result.append(seqNo)
        result.append(0x00)
        for j in range(0, 25):
            result.append(0xFF)
        while di:
            result.append(int(di[-2:], 16))
            di = di[:-2]
        cs = getCS(result)
        result.append(cs)
        result.append(0x16)
        return result

    def decodeFrame(self, data):
        # 保存数据，包含0--地址，1--数据标识，2--数据项，3--描述信息
        itemvalue = []
        array = []
        index = 0
        for j in range(0, len(data)):
            array.append(struct.unpack('B', data[j])[0])
        print array
        while index < len(array):
            if array[index] == 0xFE:
                index += 1
                break
            if array[index] == 0x68:
                index += 1
                # 表号
                MeterAddr = decodeMeterAddr(array[index:index + 4])
                # print MeterAddr
                itemvalue.append(MeterAddr)
                index += 6
                if array[index] == 0x68:
                    index += 1
                    contrlWorld = array[index]
                    # print hex(contrlWorld)
                    # 登录数据返回正常
                    if contrlWorld == 0x21:
                        itemvalue.append('')
                        itemvalue.append('')
                        itemvalue.append('登录返回正常')
                        return itemvalue
                    # 登出数据返回正常
                    elif contrlWorld == 0x22:
                        itemvalue.append('')
                        itemvalue.append('')
                        itemvalue.append('登出返回正常')
                        return itemvalue
                    # 连接返回正常
                    elif contrlWorld == 0xA5:
                        itemvalue.append('')
                        itemvalue.append('')
                        itemvalue.append('连接返回正常')
                        return itemvalue
                    # 断开连接返回正常
                    elif contrlWorld == 0xA6:
                        itemvalue.append('')
                        itemvalue.append('')
                        itemvalue.append('断开连接返回正常')
                        return itemvalue
                    # 实时召测命令正返回常
                    elif contrlWorld == 0x91:
                        index += 1
                        length = array[index]
                        index += 2
                        # 数据区域
                        dataBuf = array[index:index + length]
                        realData = []
                        for j in range(len(dataBuf) - 1, 5, -1):
                            realData.append(dataBuf[j])
                        # 数据标识
                        di = realData[-2:]
                        # print di
                        diKey = InterToHex(di)
                        # print str(diKey)
                        # 数据项
                        value = realData[:-2]
                        itemvalue.append(diKey)
                        itemvalue.append(value)
                        itemvalue.append('实时召测命令正返回常')
                        return itemvalue
                    # 读数据返回正常
                    elif contrlWorld == 0x81:
                        index += 1
                        length = array[index]
                        index += 2
                        # 数据区域
                        dataBuf = array[index:index + length]
                        # print dataBuf
                        realData = []
                        for j in range(len(dataBuf) - 1, 7, -1):
                            realData.append(dataBuf[j])
                        print realData
                        # 数据标识
                        di = realData[-2:]
                        # print di
                        diKey = InterToHex(di)
                        # print str(diKey)
                        # 数据项
                        value = realData[:-2]
                        # print value
                        itemvalue.append(diKey)
                        itemvalue.append(value)
                        itemvalue.append('读数据返回正常')
                        return itemvalue
                    # 写数据返回正常
                    elif contrlWorld == 0x88:
                        itemvalue.append('')
                        itemvalue.append('')
                        itemvalue.append('写数据返回正常')
                        return itemvalue
                    else:
                        itemvalue.append('')
                        itemvalue.append('')
                        itemvalue.append('返回异常帧')

    # 帧的头部
    def frame_top(self, terminal, msta):
        result = []
        result.append(0x68)
        temp = copy(terminal)
        while temp:
            result.append(int(temp[:2], 16))
            temp = temp[2:]
        result.append(msta)
        if self.cnt < 15:
            result.append(self.cnt)
            self.cnt += 1
        else:
            self.cnt = 0
        return result


def decodeMeterAddr(array):
    result = ''
    while array:
        if array[-1] == 0xAA:
            break
        result += hex(array[-1])
        array = array[:-1]
    return result


# 减33
def removeOffset(data):
    result = []
    for i in range(0, len(data)):
        a = data[i] - 0x33
        if a < 0:
            a += 256
        result.append(a)
    return result


# 加33
def addOffset(data):
    result = []
    for i in range(0, len(data)):
        a = data[i] + 0x33
        if a > 255:
            a -= 256
        result.append(a)
    return result


# 10进制转16进制
def InterToHex(di):
    strDi = ''
    while di:
        strDi += hex(di[0])
        di = di[1:]
    return strDi


def getCS(result):
    total = 0
    for j in range(0, len(result)):
        total += result[j]
    return total % 256
