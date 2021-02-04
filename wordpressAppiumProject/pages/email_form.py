from pages.basepage import BasePage


class EmailForm(BasePage):
    email_textbox = 'input'
    continue_button = 'login_continue_button'

    def text_email_id(self, email):
        self.page_utils.wait_element_sendtext('id', self.email_textbox, email)

    def click_continue_button(self):
        self.page_utils.wait_element_click('id', self.continue_button)
