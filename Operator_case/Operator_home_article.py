#进入文章详情页
from utils.Encapsulation_position import Action
class Op_home_article:
    def article(driver):
        Action.findXpath("//androidx.recyclerview.widget.RecyclerView[@resource-id='com.cbnweekly:id/swipe_target']/android.view.ViewGroup[1]/android.widget.ImageView[1]").click()
