# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testftplib.py
@time: 2017/3/9 19:36
@function：ftp 客户端
"""

import ftplib
import os
import socket

HOST = '192.168.0.201'
PORT = 21
DIRN = 'FTPSer'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP()
        f.connect(HOST, PORT, 30)
    except (socket.error, socket.gaierror) as e:
        print 'error'
        return
    print '*****Connection*******'

    try:
        f.login('Ye', 'aaccee')
        print f.getwelcome()
        # list = f.nlst()
        # for name in list:
        #     print (name)
        # path = 'D:/'+name
        # file = open(path,'wb')
        # filename = 'RETR '+name
        # print filename
        # f.retrbinary(filename,file.write)
        # f.delete(name)
        # f.storbinary('STOR '+filename,open(path,'rb'))
        # f.quit()
    except ftplib.error_perm:
        print 'login error'
        f.quit()
    # print '*****Logged in as '
    #
    # # try:
    # #     f.cwd(DIRN)
    # # except ftplib.error_perm:
    # #     print 'error %s' % DIRN
    # #     f.quit()
    # #     return
    # # print '*******changed to %s' % DIRN
    #
    # try:
    #     f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    # except ftplib.error_perm:
    #     os.unlink(FILE)
    #     return
    # else:
    #     print 'download %s' % FILE
    # f.quit()


if __name__ == '__main__':
    main()
