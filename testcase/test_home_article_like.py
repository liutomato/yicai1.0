'''
文章详情页点赞
author:yi
'''
import unittest
from appium import webdriver
from time import  sleep
from Operator_case.Operator_article_like import Op_like
from Operator_case.Operator_home_article import Op_home_article
from Operator_case import Operator_login_pw
class LikeTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="7.1.2"
        desired_caps["deviceName"]="127.0.0.1:21503"
        desired_caps["appPackage"]="com.cbnweekly"
        desired_caps["appActivity"]="com.cbnweekly.ui.activity.SplashActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    def test_like(self):
        '''点赞'''
                #登录
        Operator_login_pw.OP_Login_pw.test_login(self.driver)
        sleep(2)
        #点击文章
        Op_home_article.article(self.driver)
        #点赞
        Op_like.like(self.driver)