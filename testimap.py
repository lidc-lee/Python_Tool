# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testimap.py
@time: 2017/3/17 16:11
@function：imap互联网邮件访问协议
"""
import imaplib
import ConfigParser

# config = ConfigParser.ConfigParser()
# config.readfp(open('config/config.ini'), 'rb')

s = imaplib.IMAP4_SSL('imap.qq.com', 993)
print 'Connect qq mail server success'
s.login('1499117534', 'shavtqjzwgdibaba')
print 'login seccess'
rsp, msg = s.select('INBOX',True)
print rsp
print msg
print s.fetch(msg[0],'hhhh')[1]

