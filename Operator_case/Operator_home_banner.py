#首页banner 点击
from utils.Encapsulation_position import Action
class Op_home_banner:
    def test_homebanner(driver):
        u"""banner点击"""
        #Action.swipepoint(driver,178,260,600,260)
        Action.findXpath(driver,"//androidx.viewpager.widget.ViewPager[@resource-id='com.cbnweekly:id/bannerViewPager']").click()