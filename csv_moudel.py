# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: csv_moudel.py
@time: 2017/2/18 11:04
csv模块---表格数据
"""

import csv

outputFile = open('example.csv', 'w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', '1234565'])
outputFile.close()
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print exampleData