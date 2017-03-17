# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: threadPool.py
@time: 2017/3/16 15:33
@function：
"""
import concurrent.futures
from Queue import Queue
import random
import time

q = Queue()
fred = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def f(x):
    if random.randint(0, 1):
        time.sleep(0.1)
    #
    res = x * x
    q.put(res)


def main():
    # 使用线程池中4个workers处理所有job。
    # with的语句保证所有线程都执行完成后，再进行下面的操作。
    # 结果保持在一个队列中，队列是线程安全的。

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for num in fred:
            executor.submit(f, num)
    #
    while not q.empty():
        print q.get()


####################

if __name__ == "__main__":
    main()