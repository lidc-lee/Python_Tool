# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: json_moudel.py
@time: 2017/2/18 15:13
JSON
"""
import json
import requests
import sys

url = 'http://samples.openweathermap.org/data/2.5/forecast/daily?q=M%C3%BCnchen,DE&appid=b1b15e88fa797225412429c1c50c122a1'
response = requests.get(url)
response.raise_for_status()
weather = json.loads(response.text)
w = weather['list']
print w[0]['weather'][0]['main'], '--', w[0]['weather'][0]['description']
print w[1]['weather'][0]['main'], '--', w[1]['weather'][0]['description']
print w[2]['weather'][0]['main'], '--', w[2]['weather'][0]['description']