'''
首页文章详情页发表评论
@author:liu
'''
from appium import webdriver
import unittest, time
import time
from Operator_case import Operator_login_pw
from Operator_case import Operator_home_article
from Operator_case import Operator_article_comment
class CommentTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="7.1.2"
        desired_caps["deviceName"]="127.0.0.1:21503"
        desired_caps["appPackage"]="com.cbnweekly"
        desired_caps["appActivity"]="com.cbnweekly.ui.activity.SplashActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    def test_comment(self):
        u"""首页文章详情页发表评论"""
        #登录
        Operator_login_pw.OP_Login_pw.test_login(self.driver)
        time.sleep(2)
        #点击文章进入详情页面
        Operator_home_article.Op_home_article.article(self.driver)
        #评论框输入文字
        Operator_article_comment.Op_comment.article_comment(self.driver)


if __name__ == "__main__":
    unittest.main()
