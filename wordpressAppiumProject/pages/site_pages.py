from pages.basepage import BasePage


class SitePage(BasePage):
    blog = 'android.widget.TextView[text="Blog"]'
    blog_title = '//android.view.ViewGroup[contains(@content-desc,"Heading Block. Row 1. Level 2")]/android.widget.EditText'
    update = 'menu_primary_action'
    publish = 'publish_button'

    def click_blog(self):
        self.page_utils.wait_element_click('css selector', self.blog)

    def click_blog_title(self):
        self.page_utils.wait_element_click('xpath', self.blog_title)

    def text_blog_title(self, text):
        self.page_utils.wait_element_sendtext('xpath', self.blog_title, text)

    def click_update(self):
        self.page_utils.wait_element_click('id', self.update)

    def click_publish(self):
        self.page_utils.wait_element_click('id', self.publish)


