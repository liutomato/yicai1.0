#首页 搜索
import time
from appium import webdriver
from utils.Encapsulation_position import Action
class SearchTest:
    def test_search(driver):
        u"""搜索"""
        Action.findChild(driver,'com.cbnweekly:id/tabLL','首页').click()
        Action.findId(driver,'com.cbnweekly:id/search').click()
        Action.findId(driver,'com.cbnweekly:id/searchContent').send_keys('职场')