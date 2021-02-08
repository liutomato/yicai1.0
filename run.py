import pathlib
import smtplib
import time
import unittest
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from utils import HTMLTestRunner

listcase = "./testcase"
def createsuite():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listcase,pattern='test_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
def send_mail(send_user,send_pw,send_smtp,send_port,receive_user):
    flag = True
    try:
        msg = MIMEMultipart()
        # 构建正文
        mail_text = MIMEText('第一财经App1.0Android测试报告，请查收。', 'plain', 'utf-8')
        # 把正文加到邮件体里面去
        msg.attach(mail_text)
        path = os.getcwd() + '\\report'
        print(path)
        lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
        lists.sort(key=lambda fn: os.path.getctime(path + "\\" + fn), reverse=True)  # 创建时间升序
        file = os.getcwd() + '\\report\\' + lists[0]  # 取最新的文件并加上路径
        mail_file = MIMEApplication(open(file, 'rb').read())  # 打开附件
        mail_file.add_header('Content-Disposition', 'attachment', filename=pathlib.Path(file).name)  # 为附件命名
        msg.attach(mail_file)  # 添加附件

        # 发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["测试部门刘燚", send_user])
        # 收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["刘经理", receive_user])
        # 邮件的主题
        msg['Subject'] = "第一财经App1.0Android测试报告"

        # 发送邮箱按smtp配置
        server = smtplib.SMTP_SSL(send_smtp, send_port)
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(send_user, send_pw)
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(send_user, [receive_user, ], msg.as_string())
        # 关闭连接
        server.quit()
        # 如果 try 中的语句没有执行，则会执行下面的 flag=False
    except Exception:
        flag = False
    return flag

if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # os.getcwd()获取当前路径
    filename = os.getcwd() + '\\report\\' + now + "_result.html"
    fp = open(filename, 'wb')
    # print(filename)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'第一财经测试报告',
        description=u'用例执行情况')
    runner.run(createsuite())
    # 关闭文件流，不关的话生成的报告是空的
    fp.close()
    #发送邮件
    flag=send_mail('yi.liu@yoolgou.com','Ly106ly.','smtp.exmail.qq.com','465','1085195862@qq.com')
    if flag:
        print("邮件发送成功")
    else:
        print("邮件发送失败")



