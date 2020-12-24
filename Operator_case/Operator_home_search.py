#首页 搜索
import time
from appium import webdriver
from utils.Encapsulation_position import Action
class SearchTest:
    def test_search(driver):
        u"""搜索"""
        son = 'resourceId("com.cbnweekly:id/tabLL").childSelector(text("首页"))'
        driver.find_element_by_android_uiautomator(son).click()
        Action.findId(driver,'com.cbnweekly:id/search').click()
        Action.findId(driver,'com.cbnweekly:id/searchContent').send_keys('职场')