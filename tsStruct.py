# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: tsStruct.py
@time: 2017/3/2 19:44
struct模块使用
Python手册 struct 模块：http://docs.python.org/library/struct.html#module-struct
"""
import struct

# 转16进制整形
str = int('FF', 16)
# 16进制转字节流
s1 = struct.pack('B', 0xB1)
# 字节流转10进制整型
temp = struct.unpack('B', s1)
print '16进制', 0xB1, len(s1)
# 10进制转16进制
print repr(str), hex(temp[0])