import time
import unittest

from utils import HTMLTestRunner

listaa = "./testcase"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,pattern='test_home_ar*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename=now+"_result.html"
fp=open(filename,'wb')

runner= HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'第一财经测试报告',
    description=u'用例执行情况：')

runner.run(createsuite1())

#关闭文件流，不关的话生成的报告是空的
fp.close()