from pages.basepage import BasePage


class StatsPage(BasePage):
    stats_posts = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]'

    def get_stats_posts(self):
        return self.page_utils.wait_element_gettext('xpath', self.stats_posts)
