
from appium import webdriver
import unittest, time
from Operator_case import Operator_login_pw

class LoginTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="7.1.2"
        desired_caps["deviceName"]="127.0.0.1:21503"
        desired_caps["appPackage"]="com.cbnweekly"
        desired_caps["appActivity"]="com.cbnweekly.ui.activity.SplashActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    def test_login(self):
        u"""登录"""
        Operator_login_pw.OP_Login_pw.test_login(self.driver)

if __name__ == "__main__":
    unittest.main()



