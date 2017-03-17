# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: prodcons.py
@time: 2017/3/16 14:28
@function：Queue使用
"""
from myThread import MyThread
from Queue import Queue
from time import sleep
from random import randint


def writeQ(queue):
    queue.put('xxx', 1)
    # print 'writeQ', queue.qsize()


def readQ(queue):
    val = queue.get()
    print 'readQ', val


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    q = Queue(32)
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
    print 'all done'


if __name__ == '__main__':
    main()
