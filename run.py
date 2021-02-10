import pathlib
import smtplib
import time
import unittest
import os
import mail
from utils import HTMLTestRunner
import log
listcase = "./testcase"
def createsuite():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listcase,pattern='test_au*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # os.getcwd()获取当前路径
    reportfilename = os.getcwd() + '\\report\\' + now + "_result.html"
    fp = open(reportfilename, 'wb')
    # print(filename)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'第一财经测试报告',
        description=u'用例执行情况')
    runner.run(createsuite())
    # 关闭文件流，不关的话生成的报告是空的
    fp.close()
    #发送邮件
    mailclass=mail.Mail()
    flag=mailclass.send_mail('yi.liu@yoolgou.com','Ly106ly.','smtp.exmail.qq.com','465','1085195862@qq.com')
    if flag:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
    # logfilename=os.getcwd()+'\\log\\'
    # logname='第一财经杂志Android自动化测试'
    # logPrint=log.LogOutput()
    # logPrint.logOutput(logfilename,logname)



