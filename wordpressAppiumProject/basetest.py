import pytest
from actions.login_action import LoginActions
from actions.logout_action import LogoutActions
from utils.log_gen import LogGen
from utils.readExcel import ReadData


class BaseTest:

    @pytest.fixture()
    def base_test(self):
        self.logger = LogGen.log_gen()
        self.login_action = LoginActions(self.driver)
        self.logout_action = LogoutActions(self.driver)
        self.filepath = 'testdata/testdata.xlsx'
        self.login_sheet = 'login_details'
        self.email = ReadData.readData(self.filepath, self.login_sheet, 2, 1)
        self.password = ReadData.readData(self.filepath, self.login_sheet, 2, 2)
