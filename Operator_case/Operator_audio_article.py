#音频-昨夜今晨-第一篇音频 刘燚 2021.01.25

from utils.Encapsulation_position import Action
class Op_audio_article:
    def audio_article(drvier):

        #点击昨夜今晨的文章
        Action.findIds(drvier,'com.cbnweekly:id/tv_title','0').click()

