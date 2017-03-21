# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testpop3.py
@time: 2017/3/17 15:23
@function：接收邮件
"""
import poplib

HOST = 'pop.qq.com'
PORT = 995

def recevice_mail():
    pop = poplib.POP3_SSL(HOST, PORT)
    print 'Connect qq mail server success'
    pop.user('1499117534')
    pop.pass_('hyvifpdauzjeiheg')
    print 'qq mail login success'
    print pop.stat()
    msg_list = pop.list(3)
    # print type(msg_list)
    # print type(pop.retr(10))
    # 状态，消息所有行，消息的字节数
    rsp, msg, size = pop.retr(1)
    print size
    for readLine in msg:
        print readLine


if __name__ == '__main__':
    recevice_mail()