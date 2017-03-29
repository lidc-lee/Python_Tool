# coding=utf-8

"""
@version: ??
@author: AA-ldc
@file: WXPy_DB.py
@time: 2016/10/31 9:25
<p>创建一个文本框的窗口来显示鼠标的位置</p>
"""
import wx
from OperationDB import MSSQL
import re

host = '59.39.7.155:6305'
user = 'epcloudSa'
pwd = 'Hodi1234#'
db = 'Epcloud'


class MyFrame(wx.Frame):
    def __init__(self):
        """wxpython 中文前加u"""
        wx.Frame.__init__(self, None, -1, u"修改数据库app的版本号", size=(400, 400))
        panel = wx.Panel(self, -1)
        self.__getDB()
        version = self.ms.ExecQuery()
        self.text = wx.StaticText(panel, -1, "version:", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(60, 10), style=wx.TE_READONLY)
        self.posCtrl.SetValue("%s" % version)
        self.buttonRe = wx.Button(panel, label=u"刷新", pos=(200, 10), size=(50, 25))
        self.button = wx.Button(panel, label=u"修改app版本号", pos=(60, 50), size=(100, 30))
        # 绑定按钮单击事件
        self.Bind(wx.EVT_BUTTON, self.OnUpdate, self.button)
        self.Bind(wx.EVT_BUTTON, self.OnRefluse, self.buttonRe)
        self.dlg = wx.TextEntryDialog(None, u"New Version", u"是否要修改app的版本号？", '%s' % version)

    def __getDB(self):
        self.ms = MSSQL(host=host, user=user, pwd=pwd, db=db)
        self.ms.GetConnect()

    def OnUpdate(self, event):
        result = self.dlg.ShowModal()
        if result == wx.ID_OK:
            value = self.dlg.GetValue()
            m = re.match('\d.\d.\d+', value)
            if m:
                self.ms.UpdateDB(value)
                print 'OK', value
            else:
                mdlg = wx.MessageDialog(self, u"版本号格式不正确，请输入正确的格式", u"格式问题",
                                       wx.OK)
                mdlg.ShowModal()
        else:
            print 'Cancel'
            # self.dlg.Destroy()

    def OnRefluse(self, event):
        self.posCtrl.SetValue("%s" % self.ms.ExecQuery())


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
    frame.ms.close()
