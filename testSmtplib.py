# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testSmtplib.py
@time: 2017/3/17 11:26
@function：
"""
import smtplib

HOST = 'smtp.qq.com'
PORT = 465
msg = """From: test <1499117534@qq.com>
To: temp <1499117534@qq.com>
Subject: 测试邮件

这是一封测试邮件。
"""

def send_mail():
    smtpObj = smtplib.SMTP_SSL(HOST, PORT)
    ehol_result = smtpObj.ehlo()
    print ehol_result
    if int(ehol_result[0]) == 250:
        print "[Info]Connect qq mail server success."
        try:
            login_result = smtpObj.login('1499117534', 'hyvifpdauzjeiheg')
            print login_result
            if int(login_result[0]) == 235:
                print '[Info]qq mail login success.'
                send_result = smtpObj.sendmail('1499117534@qq.com', ['1499117534@qq.com'], msg)
                if send_result.__len__() == 0:
                    print '--- Send mail success.'
                else:
                    print '[Error]Send mail failed.'
                smtpObj.quit()
        except smtplib.SMTPAuthenticationError as err:
            print "[Error: smtplib.SMTPAuthenticationError]: " + str(err)
            smtpObj.quit()
    else:
        smtpObj.quit()


if __name__ == '__main__':
    send_mail()
