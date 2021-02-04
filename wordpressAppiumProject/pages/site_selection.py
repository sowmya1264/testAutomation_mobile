from pages.basepage import BasePage


class SiteSelection(BasePage):
    done_button = 'primary_button'

    def click_done_button(self):
        self.page_utils.wait_element_click('id', self.done_button)
