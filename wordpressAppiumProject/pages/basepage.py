from utils.page_utils import PageUtils


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.page_utils = PageUtils(self.driver)


