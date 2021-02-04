from pages.basepage import BasePage


class LaunchPage(BasePage):
    continue_button = 'first_button'

    def click_continue_button(self):
        self.page_utils.wait_element_click('id', self.continue_button)

    def get_pagetitle(self):
        get_title = self.page_utils.wait_element_gettext('id', self.continue_button)
        return get_title
