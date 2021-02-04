from pages.launch_page import LaunchPage
from pages.my_site import MySite
from pages.profile_settings import ProfileSettings
from utils.log_gen import LogGen


class LogoutActions:

    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.log_gen()
        self.my_site = MySite(self.driver)
        self.profile = ProfileSettings(self.driver)
        self.launch_page = LaunchPage(self.driver)

    def logout_steps(self):
        self.my_site.click_profile_button()
        self.profile.click_logout()
        self.profile.click_logout_popup()

