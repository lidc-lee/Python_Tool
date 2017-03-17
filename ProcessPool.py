# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: ProcessPool.py
@time: 2017/3/16 15:56
@function：ProcessPoolExecute是Executor的子类，使用进程池实现异步调用。ProcessPoolExecute使用多进程模块，
允许规避 Global Interpreter Lock，但是只有处理和返回picklable的对象。
"""
import sys
import redis
import concurrent.futures
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('config/config.ini'), 'rb')
HOST = '%s' % config.get('redis', 'ip')
PORT = config.get('redis', 'port')
r = redis.Redis(host=HOST, port=PORT)
fred = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def check_server():
    try:
        print r.info()
    except redis.exceptions.ConnectionError:
        print >> sys.stderr, "Error: cannot connect to redis server. Is the server running?"
        sys.exit(1)


def f(x):
    res = x * x
    r.rpush("test", res)
    # r.delete("test")

def main():
    # with 保证所有线程都执行完，再执行下面操作
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for num in fred:
            executor.submit(f, num)
    #
    print r.lrange("test", 0, -1)


####################

if __name__ == "__main__":
    check_server()
    ###
    r.delete("test")
    main()