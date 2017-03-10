# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: mtsleepD.py
@time: 2017/3/9 11:23
@function：threading
"""
import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print 'start loop %s at:' % nloop, ctime()
    sleep(nsec)
    print 'loop %s done at:' % nloop, ctime()


def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print 'all done at:', ctime()


if __name__ == '__main__':
    main()
