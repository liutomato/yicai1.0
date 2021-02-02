import time
import unittest
import os

from utils import HTMLTestRunner

listcase = "./testcase"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listcase,pattern='test_home_s*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
#os.getcwd()获取当前路径1
filename=os.getcwd()+'\\report\\'+now+"_result.html"
fp=open(filename,'wb')
# print(filename)
runner= HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'第一财经测试报告',
    description=u'用例执行情况')

runner.run(createsuite1())

#关闭文件流，不关的话生成的报告是空的
fp.close()

