'''点赞'''
from utils.Encapsulation_position import Action
from time import sleep
class Op_like:
    def like(driver):
        #滑动页面至找到点赞按钮
        flag=True
        while flag:
            try:
                Action.findId(driver,'com.cbnweekly:id/like').click()
                flag=False
            except:
                Action.swipeUp(driver)

        sleep(6)
