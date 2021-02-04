from time import sleep
import pytest
from pages.email_form import EmailForm
from pages.login_form import LoginForm
from pages.site_selection import SiteSelection
from utils.readExcel import ReadData
from actions.logout_action import LogoutActions
from pages.launch_page import LaunchPage
from pages.my_site import MySite
from basetest import BaseTest

#This test case is to verify the valid and invalid login scenarios
class TestLoginScenarios(BaseTest):

    @pytest.mark.sanity
    def test_login_scenarios(self, setup, base_test):
        self.driver = setup
        self.my_site = MySite(self.driver)
        self.logout_action = LogoutActions(self.driver)
        self.launch_page = LaunchPage(self.driver)
        self.email_form = EmailForm(self.driver)
        self.login_form = LoginForm(self.driver)
        self.site_selection = SiteSelection(self.driver)

        # read excel and get the row count
        # self.filepath = '../testdata/testdata.xlsx'
        self.tc_sheet = 'login_scenarios'
        self.col_cnt = ReadData.getColCount(self.filepath, self.tc_sheet)
        self.row_cnt = ReadData.getRowCount(self.filepath, self.tc_sheet)

        for r in range(2, self.row_cnt + 1):
            # read values from excel
            self.logger.info(f"Testing for test data {r - 1}")
            self.email = ReadData.readData(self.filepath, self.tc_sheet, r, 2)
            self.password = ReadData.readData(self.filepath, self.tc_sheet, r, 3)
            self.exptitle = ReadData.readData(self.filepath, self.tc_sheet, r, 4)
            self.expresult = ReadData.readData(self.filepath, self.tc_sheet, r, 5)

            # login actions
            self.launch_page.click_continue_button()
            self.email_form.text_email_id(self.email)
            self.email_form.click_continue_button()
            self.login_form.text_pwd(self.password)
            self.login_form.click_continue_button()
            sleep(5)
            page_header = self.my_site.get_page_header()

            if page_header != 'Log In':
                self.site_selection.click_done_button()
                # verify the title after login
                self.act_title = self.my_site.get_title()
                if self.act_title == self.exptitle:
                    # pass login for valid data
                    if self.expresult == "login success":
                        assert True
                        self.logger.info("*** test case pass as login success for valid data***")
                        ReadData.writeData(self.filepath, self.tc_sheet, r, 6, "Pass")
                        self.logout_action.logout_steps()
                    # fail login for valid data
                    elif self.expresult == "login fail":
                        assert False
                        self.logger.info("***test case fail as login success for invalid data***")
                        ReadData.writeData(self.filepath, self.tc_sheet, r, 6, "Fail")
                        self.logout_action.logout_steps()

            else:
                self.driver.back()
                self.driver.back()
                if self.expresult == "login fail":
                    self.logger.info("*** test case pass as login fail for in valid data***")
                    ReadData.writeData(self.filepath, self.tc_sheet, r, 6, "Pass")
                    assert True
                else:
                    self.logger.info("*** test case fail as login fail for in valid data***")
                    ReadData.writeData(self.filepath, self.tc_sheet, r, 6, "Fail")
                    assert False
