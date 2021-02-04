from pages.basepage import BasePage


class LoginForm(BasePage):
    pwd_textbox = 'input'
    continue_button = 'primary_button'

    def text_pwd(self, password):
        self.page_utils.wait_element_sendtext('id', self.pwd_textbox, password)

    def click_continue_button(self):
        self.page_utils.wait_element_click('id', self.continue_button)
