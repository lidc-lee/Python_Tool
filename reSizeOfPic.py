# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: reSizeOfPic.py
@time: 2017/5/19 19:39
@function：批量修改图片的大小
"""

import sys
import os,glob
import platform
import urllib2

import StringIO
import win32file, win32con
from PIL import Image
from send2trash import send2trash

reload(sys)
sys.setdefaultencoding('utf-8')

# new_width =2048
# width =int(raw_input("the width U want:"))
# imgslist = glob.glob(path+'/*.*')

ShuiPing = "水平"
ShiZhuang = "矢状"
GuanZhuang = "冠状"


def Py_Log(_string):
    print "----" + _string.decode('utf-8') + "----"


def is_windows_system():
    return 'Windows' in platform.system()


def is_hiden_file(file_Path):
    if is_windows_system():
        fileAttr = win32file.GetFileAttributes(file_Path)
        if fileAttr & win32con.FILE_ATTRIBUTE_HIDDEN:
            return True
        return False
    return False


def remove_hidden_file(file_path):
    send2trash(file_path)
    print "Delete hidden file path:" + file_path


def astrcmp(str1, str2):
    return str1.lower() == str2.lower()


def resize_image(img_path):
    try:
        mPath, ext = os.path.splitext(img_path)
        if astrcmp(ext, ".png") or astrcmp(ext, ".jpg"):
            img = Image.open(img_path)
            (width, height) = img.size

            if width != new_width:
                new_height = int(height * new_width / width)
                out = img.resize((new_width, new_height), Image.ANTIALIAS)
                new_file_name = '%s%s' % (mPath, ext)
                out.save(new_file_name, quality=100)
                Py_Log("图片尺寸修改为：" + str(new_width))
            else:
                Py_Log("图片尺寸正确，未修改")
        else:
            Py_Log("非图片格式")
    except Exception, e:
        print e

        # 改变图片类型


def change_img_type(img_path):
    try:
        img = Image.open(img_path)
        img.save('new_type.png')
    except Exception, e:
        print e

        # 处理远程图片
def handle_remote_img(img_url):
    try:
        request = urllib2.Request(img_url)
        img_data = urllib2.urlopen(request).read()
        img_buffer = StringIO.StringIO(img_data)
        img = Image.open(img_buffer)
        img.save('remote.jpg')
        (width, height) = img.size
        out = img.resize((200, height * 200 / width), Image.ANTIALIAS)
        out.save('remote_small.jpg')
    except Exception, e:
        print e


def rename_forder(forder_path):
    Py_Log("------------rename_forder--------------------------")
    names = os.path.split(forder_path)
    try:
        if (unicode(ShuiPing) in unicode(names[1], 'gbk')):
            os.rename(forder_path, names[0] + "\\" + "01")
            Py_Log(names[1] + "-->" + "01")
        if (unicode(ShiZhuang) in unicode(names[1], 'gbk')):
            os.rename(forder_path, names[0] + "\\" + "02")
            Py_Log(names[1] + "-->" + "02")
        if (unicode(GuanZhuang) in unicode(names[1], 'gbk')):
            os.rename(forder_path, names[0] + "\\" + "03")
            Py_Log(names[1] + "-->" + "03")
    except Exception, e:
        print e


def BFS_Dir(dirPath, dirCallback=None, fileCallback=None):
    queue = []
    ret = []
    queue.append(dirPath);
    while len(queue) > 0:
        tmp = queue.pop(0)
        if (os.path.isdir(tmp)):
            ret.append(tmp)
            for item in os.listdir(tmp):
                queue.append(os.path.join(tmp, item))
            if dirCallback:
                dirCallback(tmp)
        elif (os.path.isfile(tmp)):
            ret.append(tmp)
            if fileCallback:
                fileCallback(tmp)
    return ret


def DFS_Dir(dirPath, dirCallback=None, fileCallback=None):
    stack = []
    ret = []
    stack.append(dirPath);
    while len(stack) > 0:
        tmp = stack.pop(len(stack) - 1)
        if (os.path.isdir(tmp)):
            ret.append(tmp)
            for item in os.listdir(tmp):
                stack.append(os.path.join(tmp, item))
            if dirCallback:
                dirCallback(tmp)
        elif (os.path.isfile(tmp)):
            ret.append(tmp)
            if fileCallback:
                fileCallback(tmp)
    return ret


def printDir(dirPath):
    print "dir: " + dirPath
    if (is_hiden_file(dirPath)):
        remove_hidden_file(dirPath)
    else:
        rename_forder(dirPath)


def printFile(dirPath):
    print "file: " + dirPath
    resize_image(dirPath)
    return True


if __name__ == '__main__':
    while True:
        path = raw_input("Path:")
        new_width = int(raw_input("the width U want:"))
        try:
            b = BFS_Dir(path, printDir, printFile)
            Py_Log("\r\n          **********\r\n" + "*********图片处理完毕*********" + "\r\n          **********\r\n")
        except:
            print "Unexpected error:", sys.exc_info()
        raw_input('press enter key to rehandle')