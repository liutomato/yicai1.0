#首次进入app跳过隐私条款弹窗
from utils.Encapsulation_position import Action
class Op_popup:
    def Op_popup(driver):
        Action.findId(driver,'com.cbnweekly:id/know').click()

