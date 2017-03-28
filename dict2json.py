# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: dict2json.py
@time: 2017/3/28 15:19
@function：python字典转json
"""
from distutils.log import warn as printf
from json import dumps
from pprint import pprint

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
printf('***RWA DICT***')
printf(BOOKs)

printf('***RWA JSON***')
printf(dumps(BOOKs))

printf(dumps(BOOKs, indent=4))
