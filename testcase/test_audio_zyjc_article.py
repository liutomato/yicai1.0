#进入音频-作昨夜今晨-点击第一篇文章
import traceback

from appium import webdriver
import unittest, time
from Operator_case import Operator_audio
from Operator_case import Operator_audio_zyjc
from Operator_case import Operator_popup
from Operator_case import Operator_audio_article
from Operator_case import Operator_audio_article_zhankai
from utils import Encapsulation_position
class Playertest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="7.1.2"
        desired_caps["deviceName"]="127.0.0.1:21503"
        desired_caps["appPackage"]="com.cbnweekly"
        desired_caps["appActivity"]="com.cbnweekly.ui.activity.SplashActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    def test_player(self):

        u'''进入音频-作昨夜今晨'''
        print(2)
        #调过隐私条款弹窗
        Operator_popup.Op_popup.Op_popup(self.driver)
        #进入音频模块
        Operator_audio.Op_audio.Op_audio(self.driver)
        #进入昨夜今晨栏目合集
        Operator_audio_zyjc.Op_audio_zyjc.audio_zyjc(self.driver)
        #进入第一篇文章
        Operator_audio_article.Op_audio_article.audio_article(self.driver)
        #点击展开按钮
        Operator_audio_article_zhankai.Op_zhankai.Op_zhankai(self.driver)
        Encapsulation_position.Action.savescreenshot(self.driver)

if __name__ == '__main__':
    unittest.main()
