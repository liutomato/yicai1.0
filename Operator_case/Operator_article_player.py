#播放器操作 20210128 liuyi
from utils.Encapsulation_position import Action
class Op_player:
    def Op_player(driver):
        #点击播放按钮
        Action.findId(driver,'com.cbnweekly:id/im_bf').click()
        #点击下一篇
        Action.findId(driver,'com.cbnweekly:id/im_next').click()
        #点击上一篇
        Action.findId(driver,'com.cbnweekly:id/im_last').click()
        