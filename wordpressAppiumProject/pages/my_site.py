from pages.basepage import BasePage


class MySite(BasePage):
    title = 'my_site_title_label'
    profile = 'avatar'
    posts = 'quick_action_posts_button'
    stats = 'my_site_stats_text_view'
    pages = 'quick_action_pages_button'
    blog_url = 'my_site_subtitle_label'
    page_header = 'android.widget.TextView'

    def get_title(self):
        title_value = self.page_utils.wait_element_gettext('id', self.title)
        return title_value

    def click_profile_button(self):
        self.page_utils.wait_element_click('id', self.profile)

    def click_posts(self):
        self.page_utils.wait_element_click('id', self.posts)

    def click_stats(self):
        self.page_utils.wait_element_click('id', self.stats)

    def click_pages(self):
        self.page_utils.wait_element_click('id', self.pages)

    def click_blog_url(self):
        self.page_utils.wait_element_click('id', self.blog_url)

    def get_page_header(self):
        return self.page_utils.wait_element_gettext('class name', self.page_header)


