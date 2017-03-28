# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: myhttpd.py
@time: 2017/3/23 14:12
@function：编写一个简单的web服务器
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found:%s' % self.path)


def main():
    try:
        server = HTTPServer(('', 8088), MyHandler)
        print 'Welcome'
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

import os
if __name__ == '__main__':
    main()
    os.uname()[0]


