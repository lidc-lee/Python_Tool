# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: friendA.py
@time: 2017/3/23 16:03
@function：CGI
"""
import cgi

reshtml = '''Content-Type:text/html\n
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>欢迎来到CGI</title>
</head>
<body>
Hello,<B>%s</B>,<B>%s</B>
</body>
</html>
'''
form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print reshtml % (who, howmany)
