from pages.basepage import BasePage


class BlogPublish(BasePage):
    blogtitle = 'android.widget.EditText[text="Add title"]'
    blogtext = 'android.widget.EditText[text="Start writing…"]'
    publish = 'android.widget.TextView[text="PUBLISH"]'
    publishnow = 'android.widget.Button[text="PUBLISH NOW"]'
    confirm_msg = 'android.widget.TextView[text="Post published"]'

    def text_blog_title(self, exp_title):
        self.page_utils.wait_element_sendtext('css selector', self.blogtitle, exp_title)

    def text_blog_text(self, exp_text):
        self.page_utils.wait_element_sendtext('css selector', self.blogtext, exp_text)

    def click_publish(self):
        self.page_utils.wait_element_click('css selector', self.publish)

    def click_publishnow(self):
        self.page_utils.wait_element_click('css selector', self.publishnow)

    def get_confirm_msg(self):
        get_msg = self.page_utils.wait_element_gettext('css selector', self.confirm_msg)
        return get_msg

