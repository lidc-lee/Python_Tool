# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: batch_file_rename.py
@time: 2017/2/16 14:45
重命名
"""
import os
import sys
import argparse


def batch_rename(work_dir, old_ext, new_ext):
    # 指定目录的所有文件名
    # print os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # 分离文件名和后缀
        file_ext = os.path.splitext(filename)[0]
        if old_ext == file_ext:
            name_list = list(filename)
            name_list[len(name_list) - len(old_ext):] = list(new_ext)
            newfile = ''.join(name_list)
            print newfile
            os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile))


def main():
    batch_rename('.', 'app-hodi', 'app-hodiTest.apk')


if __name__ == '__main__':
    main()
