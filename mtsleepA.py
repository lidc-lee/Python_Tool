# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: mtsleepA.py
@time: 2017/3/9 11:23
@function：多线程并发执行
"""
import thread
from time import sleep, ctime


def loop0():
    print 'start loop0 at:', ctime()
    sleep(4)
    print 'loop0 done at:', ctime()


def loop1():
    print 'start loop1 at:', ctime()
    sleep(2)
    print 'loop1 done at:', ctime()


def main():
    print 'starting at:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all done at:', ctime()


if __name__ == '__main__':
    main()
