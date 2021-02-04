from time import sleep
import pytest
from pages.profile_settings import ProfileSettings
from pages.my_site import MySite
from pages.my_profile import MyProfile
from utils.readExcel import ReadData
from basetest import BaseTest

#This text case is to verify the edit function of the diaply name under my profile page
class TestEditName(BaseTest):

    @pytest.mark.regression
    def test_edit_name(self, setup, base_test):
        self.driver = setup
        self.my_site = MySite(self.driver)
        self.profile = ProfileSettings(self.driver)
        self.my_profile = MyProfile(self.driver)

        self.tc_sheet = 'edit_name'
        self.new_displayname = ReadData.readData(self.filepath, self.tc_sheet, 2, 1)

        # login function
        self.login_action.login_steps(self.email, self.password)
        self.logger.info("***Login Successful***")

        # Navigate to profile page
        self.my_site.click_profile_button()
        self.profile.click_my_profile()
        self.logger.info("***Navigated to my profile page***")

        # Edit the display name

        self.my_profile.click_display_name()
        self.my_profile.clear_display_name()
        self.my_profile.text_display_name(self.new_displayname)
        self.my_profile.click_ok()
        sleep(3)
        self.logger.info("***Edited the display name***")

        # Navigate to profile page

        self.driver.back()
        self.logger.info("***Navigated back to profile page***")
        actual_displayname = self.profile.get_display_name()
        self.logger.info(f"Actual display name after updating is {actual_displayname}")

        # validate confirmation message
        if actual_displayname == self.new_displayname:
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 2, actual_displayname)
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 3, "Pass")
            self.logger.info(f"new blog title {self.new_displayname} is updated correctly in web view")
            self.profile.click_logout()
            self.profile.click_logout_popup()
            self.driver.quit()
            self.logger.info("***Logout Successful***")
            assert True
        else:
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 2, actual_displayname)
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 3, "Fail")
            self.logger.info(f"new blog title {self.new_displayname} is not updated in web view")
            self.profile.click_logout()
            self.profile.click_logout_popup()
            self.driver.quit()
            self.logger.info("***Logout Successful***")
            assert False
