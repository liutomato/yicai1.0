#文章详情页发表评论
from utils.Encapsulation_position import Action
from time import sleep
class Op_comment:
    def article_comment(driver):
        Action.findId(driver,'com.cbnweekly:id/commentContent').click()
        Action.findId(driver,'com.cbnweekly:id/commentContent').send_keys('观点很新颖')
        sleep(2)
        driver.press_keycode(66)

