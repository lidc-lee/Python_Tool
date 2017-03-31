# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testWSGI.py
@time: 2017/3/30 10:40
@function：测试wsgi
"""
from wsgiref.simple_server import make_server, demo_app


def simple_wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [u'hello world,我是大东！！！！！！！！'.encode('gbk')]


httpd = make_server('192.168.0.75', 8888, simple_wsgi_app)
print "started app serving on port 8888"
httpd.serve_forever()
