# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: onethr.py
@time: 2017/3/9 10:54
@function：单线程执行循环
"""
from time import ctime, sleep


def loop0():
    print 'start loop0 at:', ctime()
    sleep(4)
    print 'loop0 done at:', ctime()


def loop1():
    print 'start loop1 at:', ctime()
    sleep(2)
    print 'start loop1 at:', ctime()


def main():
    print 'starting at:', ctime()
    loop0()
    loop1()
    print 'all done at:', ctime()


if __name__ == '__main__':
    main()
