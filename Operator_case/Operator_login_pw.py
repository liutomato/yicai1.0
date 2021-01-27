#账号 密码登录

from utils.Encapsulation_position import Action
class OP_Login_pw:
    def test_login(driver):
        u"""登录"""
        print(111)
        Action.findChild(driver,'com.cbnweekly:id/tabLL','我的').click()
        Action.findId(driver,'com.cbnweekly:id/editData').click()#我的资料
        Action.findId(driver,'com.cbnweekly:id/changeLoginModel').click()#切换至账号密码登录
        Action.findId(driver,'com.cbnweekly:id/account').send_keys('15222574399')
        Action.findId(driver,'com.cbnweekly:id/password').send_keys('1234qwer')
        Action.findId(driver,'com.cbnweekly:id/btn').click()#点击登录

        # driver.find_element_by_id('com.cbnweekly:id/editData').click()
        # time.sleep(2)
        # driver.find_element_by_id('com.cbnweekly:id/changeLoginModel').click()
        # time.sleep(2)
        # driver.find_element_by_id('com.cbnweekly:id/account').send_keys('15222574399')
        # driver.find_element_by_id('com.cbnweekly:id/password').send_keys('1234qwer')
        # time.sleep(3)
        # driver.find_element_by_id('com.cbnweekly:id/btn').click()