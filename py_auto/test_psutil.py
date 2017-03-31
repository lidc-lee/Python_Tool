# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: test_psutil.py
@time: 2017/3/31 10:57
@function：psutil模块的使用
"""
import psutil
import datetime

print '\n****************************内存信息*****************************'
# 使用cpu_times方法获取cpu的完整信息
print psutil.cpu_times()
# 指定方法变量
print psutil.cpu_times(percpu=True)
# user的CPU时间比
print psutil.cpu_times().user
# 获取cpu的逻辑个数，默认logical=True
print psutil.cpu_count(logical=True)
# 物理个数
print psutil.cpu_count(logical=False)
# 内存信息
men = psutil.virtual_memory()
print men
print men.total
print men.free
# 获取分区信息
print psutil.swap_memory()

print '\n*******************磁盘信息***************'
# 获取磁盘完整信息
disk = psutil.disk_partitions()
print disk
# 分区信息
print psutil.disk_usage('/')
# 硬盘的总io数,read_count--读IO数，write_count--写IO数，read_bytes--读字节数，
# write_bytes--写字节数，read_time--磁盘读时间，write_time--写时间
print psutil.disk_io_counters()
# 获取单个分区IO个数
print psutil.disk_io_counters(perdisk=True)
# 网络信息
# 获取网络总的IO信息,默认pernic=False
# bytes_sent--发送字节, bytes_recv--接收字节, packets_sent--发送数据包, packets_recv--接收数据包
print psutil.net_io_counters(pernic=False)
# 每个网络接口的IO信息
print psutil.net_io_counters(pernic=True)
# 当前登陆系统的用户信息
print psutil.users()
# 开机时间
t = psutil.boot_time()
print datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")

print '\n************************进程信息******************************'
# 所有进程PID
print psutil.pids()

p = psutil.Process(pid=2880)
print p.name()
# 进程bin的路径
# print p.exe()
print p.status()
# print p.cwd()
print datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
# print p.uids()
# print p.gids()
print p.cpu_times()
# print p.cpu_affinity()
print p.memory_percent() #内存利用率
print p.connections()
print p.num_threads() #进程开启的线程数

# print '\n***************popen类*********************'
# popen = psutil.Popen()