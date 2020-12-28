#首页信息流滑动
from appium import webdriver
import unittest, time
from utils.Encapsulation_position import Action

class HomeswipeTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="7.1.2"
        desired_caps["deviceName"]="127.0.0.1:21503"
        desired_caps["appPackage"]="com.cbnweekly"
        desired_caps["appActivity"]="com.cbnweekly.ui.activity.SplashActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    def test_homeswipe(self):
        u"""首页信息流滑动"""
        time.sleep(5)
        Action.swipeUp(self.driver)