#进入音频模块 刘燚 2021.01.26
from utils.Encapsulation_position import Action
class Op_audio:
    def Op_audio(drvier):
        Action.findChild(drvier, 'com.cbnweekly:id/tabLL', '音频').click()
