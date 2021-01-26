#音频-昨夜今晨 刘燚 2021.01.25

from utils.Encapsulation_position import Action
class Op_audio_zyjc:
    def audio_zyjc(drvier):
        #点击昨夜今晨
        Action.findIds(drvier,'com.cbnweekly:id/im_logo','0').click()
