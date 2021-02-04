from time import sleep

import pytest

from pages.profile_settings import ProfileSettings
from pages.site_pages import SitePage
from pages.webview import WebView
from pages.my_site import MySite
from utils.readExcel import ReadData
from basetest import BaseTest

# This test case is to verify if the blog web view displays the correct blog title when it is updated from the app
class TestBlogTitleWebview(BaseTest):

    @pytest.mark.sanity
    def test_blog_webview(self, setup, base_test):
        self.driver = setup
        self.my_site = MySite(self.driver)
        self.profile = ProfileSettings(self.driver)
        self.site_pages = SitePage(self.driver)
        self.webview = WebView(self.driver)

        self.tc_sheet = 'blogtitle_webview'
        self.new_blogtitle = ReadData.readData(self.filepath, self.tc_sheet, 2, 1)

        # login function
        self.login_action.login_steps(self.email, self.password)
        self.logger.info("***Login Successful***")

        # Navigate to site page
        self.my_site.click_pages()

        # click on blog
        self.site_pages.click_blog()

        # Edit and update the blog title
        self.site_pages.click_blog_title()
        self.site_pages.click_blog_title()
        self.site_pages.text_blog_title(self.new_blogtitle)
        self.site_pages.click_update()
        self.site_pages.click_publish()
        self.logger.info("***Blog title updated in app***")

        # Navigate to my site page
        sleep(5)
        self.driver.back()

        # blog url redirects to the webview
        self.my_site.click_blog_url()

        # get the open contexts
        sleep(5)
        contexts = self.driver.contexts

        # Navigate to the webview context
        sleep(5)
        self.driver.switch_to.context(contexts[1])
        self.logger.info("***Navigated to the Webview***")

        # Get the blog title
        self.webview.click_menu()
        self.webview.click_menu_item()
        blog_title_site = self.webview.get_blog_title_site()
        self.logger.info(f"The blog title shown in webview is {blog_title_site}")

        # Navigate back to native app
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.switch_to.context('NATIVE_APP')
        self.logger.info("***Navigated to the native app***")

        # validate confirmation message
        if blog_title_site == self.new_blogtitle:
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 2, blog_title_site)
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 3, "Pass")
            self.logger.info(f"new blog title {self.new_blogtitle} is updated correctly in web view")
            self.driver.back()
            self.logout_action.logout_steps()
            self.logger.info("***Logout Successful***")
            assert True
        else:
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 2, blog_title_site)
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 3, "Fail")
            self.logger.info(f"new blog title {self.new_blogtitle} is not updated in web view")
            self.driver.back()
            self.logout_action.logout_steps()
            self.logger.info("***Logout Successful***")
            assert False

        # logout function
