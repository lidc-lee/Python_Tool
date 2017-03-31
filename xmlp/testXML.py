# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testXML.py
@time: 2017/3/30 14:50
@function：字典转换成xml
"""
from xml.etree.ElementTree import Element,SubElement,tostring
from xml.dom.minidom import parseString

BOOKs = {
    '0001': {
        'title': 'ldc',
        'edition': 2,
        'year': 2017
    },
    '0002': {
        'title': 'lwl',
        'edition': 5,
        'year': 2017
    },
    '0003': {
        'title': 'ljk',
        'edition': 6,
        'year': 2016
    }
}
books = Element('books')
for isbn,info in BOOKs.iteritems():
    book = SubElement(books,'book')
    info.setdefault('edition',1)
    info.setdefault('authors','lee')
    for key,val in info.iteritems():
        SubElement(book,key).text = ','.join(str(val).split(':'))
xml = tostring(books)
# print '***XML***'
# print xml

dom = parseString(xml)
print dom.toprettyxml('  ')