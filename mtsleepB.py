# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: mtsleepA.py
@time: 2017/3/9 11:23
@function：多线程并发执行引入锁
"""
import thread
from time import sleep, ctime

loops = [4, 2, 3]


def loop(nloop, nsec, lock):
    print 'start loop %s at:' % nloop, ctime()
    sleep(nsec)
    print 'loop %s done at:' % nloop, ctime()
    lock.release()


def main():
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    print 'all done at:', ctime()


if __name__ == '__main__':
    main()
