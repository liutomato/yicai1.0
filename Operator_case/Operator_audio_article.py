#音频-昨夜今晨-第一篇音频 刘燚 2021.01.25

from utils.Encapsulation_position import Action
class Op_audio_article:
    def audio_article(drvier):
        Action.findChild(drvier,'com.cbnweekly:id/tabLL','音频').click()
        Action.findIds(drvier,'com.cbnweekly:id/im_logo','0').click()

