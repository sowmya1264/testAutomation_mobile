from pages.basepage import BasePage


class WebView(BasePage):
    menu = '//*[@id="site-navigation"]'
    menu_item = 'Blog'
    blog_title = '//*[@id=\"post-6\"]/div/div[1]/div/h2'

    def click_menu(self):
        self.page_utils.wait_element_click('xpath', self.menu)

    def click_menu_item(self):
        self.page_utils.wait_element_click('link text', self.menu_item)


    def get_blog_title_site(self):
        return self.page_utils.wait_element_gettext('xpath', self.blog_title)



