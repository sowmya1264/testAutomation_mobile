from pages.basepage import BasePage


class ProfileSettings(BasePage):
    logout = 'me_login_logout_text_view'
    logout_popup = 'android.widget.Button[id="button1"]'
    my_profile = 'me_my_profile_text_view'
    profile_display_name = 'me_display_name'

    def click_logout(self):
        self.page_utils.wait_element_click('id', self.logout)

    def click_logout_popup(self):
        self.page_utils.wait_element_click('css selector', self.logout_popup)

    def click_my_profile(self):
        self.page_utils.wait_element_click('id', self.my_profile)

    def get_display_name(self):
        name = self.page_utils.wait_element_gettext('id', self.profile_display_name)
        return name
