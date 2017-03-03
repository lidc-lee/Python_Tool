# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: hodi_frame.py
@time: 2017/3/1 19:15
协议帧工厂方法模式
"""

import struct
from copy import *


# 简单工厂
class FrameFather():
    def __init__(self):
        pass

    # 解帧方法
    def decodeFrame(self, FrameType):
        pass

    # 组帧方法
    def encodeFrame(self, FrameType):
        pass


class FrameFactory():
    DOWM_FRAME_PROCOTL = 1
    UP_FRAME_PROCOTL = 2

    # 构造方法
    def __init__(self):
        print "构造方法"

    def getCS(self, result):
        total = 0
        for i in range(0, len(result)):
            total += result[i]
        return total % 256

    # # 解帧方法
    # def decodeFrame(self, FrameType):
    #
    #     if FrameType == 1:
    #         print "下行协议--解帧方法"
    #     else:
    #         print "上行协议--解帧方法"

    # 组帧方法
    def encodeFrame(self, FrameType):
        if FrameType == 1:
            print "下行协议--组帧方法"
        else:
            print "上行协议--组帧方法"

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
        cs = self.getCS(result[2:])
        result.append(cs)
        result.append(0x16)
        return result

    # 读后续数据的组帧方法
    def encodeLaterReadFrame(self, meterAddress, di):
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
        result.append(0x02)
        result.append(0x02)
        while di:
            result.append(int(di[len(di) - 2:], 16) + 0x33)
            di = di[:len(di) - 2]
        cs = self.getCS(result[2:])
        result.append(cs)
        result.append(0x16)
        return result

    # 重读
    def encodeReReadFrame(self, meterAddress):
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
        result.append(0x03)
        result.append(0x00)
        cs = self.getCS(result[2:])
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
        cs = self.getCS(result[2:])
        result.append(cs)
        result.append(0x16)
        return result

    # 解帧
    def decodeFrame(self, data):
        array = []
        index = 0
        for i in range(0, len(data)):
            array.append(struct.unpack('B', data[i])[0])
        print array

        while index < len(array):
            if array[index] == 0xFE:
                index += 1
                break
            if array[index] == 0x68:
                index += 1
                # 表地址
                MeterAddr = self.decodeMeterAddr(array[index:index + 6])
                print str(meterAddr)
                index += 6
                if array[index] == 0x68:
                    index += 1
                    contrlWorld = array[index]
                    print hex(contrlWorld)
                    if contrlWorld == 0x81:
                        index += 1
                        # 数据域的长度
                        length = array[index]
                        print length
                        index += 1
                        dataBuf = self.removeOffset(array[index:index + length])
                        print dataBuf

    def decodeMeterAddr(self, array):
        result = ''
        while array:
            result = result + hex(array[-1])
            array = array[:-1]
        return result

    def removeOffset(self, data):
        result = []
        for i in range(0, len(data)):
            a = data[i] - 0x33
            if a<0:
                a += 256
            result.append(a)
        return result


if __name__ == '__main__':
    frameFactory = FrameFactory()
    frameFactory.encodeFrame(frameFactory.DOWM_FRAME_PROCOTL)
    # frameFactory.decodeFrame(frameFactory.UP_FRAME_PROCOTL)
    # frameFactory.decodeFrame(frameFactory.DOWM_FRAME_PROCOTL)
    meterAddr = '33304552'
    result1 = frameFactory.encodeReadFrame(meterAddr, '8010')
    data = ['02', 'AA', 'AA', 'DB', '80', '7D', '62', '26', '49']
    result2 = frameFactory.encodeWriteFrame(meterAddr, data, 9, '8010')
    print result1
    print result2
    hexStr = ''
    for i in range(0, len(result2)):
        hexStr += hex(result2[i])
    print hexStr.upper().split('0X')
    array = []
    result3 = ['68', '76', '45', '30', '33', '16', '52', '68', '81', '0B', '43', 'B3', '81', '25', '9B', '07', '27',
               '3B', 'DD', 'DD', '35', '71', '16']
    result4 = []
    for i in range(0, len(result3)):
        result4.append(int(result3[i], 16))
        array.append(struct.pack('B', result4[i]))
    frameFactory.decodeFrame(array)
