# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: sys_moudel.py
@time: 2017/2/17 17:08
sys的使用
"""
import sys

# 脚本名称
print 'name is', sys.argv[0]


# 脚本路劲
# print 'path is ', sys.path

# 使用sys模块查找内建模块
def dump(module):
    print module, "=>"
    if module in sys.builtin_module_names:  # 查找内建模块是否存在
        print '内建模块'
    else:
        module = __import__(module)
        print module


dump("os")
dump('sys')
dump('string')
# 输入流
line1 = sys.stdin.readline()
print len(line1)
