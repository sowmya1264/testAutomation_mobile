from pages.basepage import BasePage


class MyProfile(BasePage):
    display_name = 'display_name_row'
    display_name_edit = 'text_input_dialog_input'
    ok_popup = 'android.widget.Button[text="OK"]'


    def click_display_name(self):
        self.page_utils.wait_element_click('id', self.display_name)

    def clear_display_name(self):
        self.page_utils.wait_element_clear('id', self.display_name_edit)

    def text_display_name(self, text):
        self.page_utils.wait_element_sendtext('id', self.display_name_edit, text)

    def click_ok(self):
        self.page_utils.wait_element_click('css selector', self.ok_popup)
