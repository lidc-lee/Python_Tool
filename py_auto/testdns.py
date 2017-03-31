# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testdns.py
@time: 2017/3/31 15:07
@function：dnspython模块使用
"""
import testdns2.resolver

# print '***********A************'
# domain = raw_input('Please input an domain: ')
#
# A = dns.resolver.query(domain, 'A')
# for i in A.response.answer:
#     for j in i.items:
#         print j.address

# print '***********MX************'
# domain = raw_input('Please input an domain: ')
#
# MX = dns.resolver.query(domain, 'MX')
# for i in MX:
#     print 'MX preference =', i.preference, 'mail exchanger =', i.exchange

# print '*************NS****************'
# domain = raw_input('Please input an domain: ')
# ns = dns.resolver.query(domain, 'NS')
# for i in ns.response.answer:
#      for j in i.items:
#           print j.to_text()

print '****************CNAME****************'
domain = raw_input('Please input an domain: ')

cname = testdns2.resolver.query(domain, 'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()