# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testbs4.py
@time: 2017/3/31 16:57
@function：beautifulsoup
"""
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup1 = BeautifulSoup(html_doc, 'html.parser')
soup2 = BeautifulSoup(html_doc, 'lxml')
soup3 = BeautifulSoup(html_doc, 'xml')
soup4 = BeautifulSoup(html_doc, 'html5lib')
# print soup1
# print soup2
# print soup3
# print soup4
tag = soup4.p
print type(tag)
print tag.attrs
print tag['class']
print tag.string
list = soup4.find_all('a')
print list[0]

