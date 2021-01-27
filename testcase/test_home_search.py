#登陆后搜索
from appium import webdriver
import unittest, time
import time
from Operator_case import Operator_home_search
from Operator_case import Operator_login_pw
class SearchTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="7.1.2"
        desired_caps["deviceName"]="127.0.0.1:21503"
        desired_caps["appPackage"]="com.cbnweekly"
        desired_caps["appActivity"]="com.cbnweekly.ui.activity.SplashActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    def test_search(self):
        u"""搜索"""
        # #登录
        # Operator_login_pw.OP_Login_pw.test_login(self.driver)
        time.sleep(2)
        #搜索
        Operator_home_search.SearchTest.test_search(self.driver)


if __name__ == "__main__":
    unittest.main()
