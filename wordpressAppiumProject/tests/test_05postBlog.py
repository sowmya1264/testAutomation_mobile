from time import sleep

import pytest

from pages.blog_posts import BlogPosts
from pages.blog_publish import BlogPublish
from pages.my_site import MySite
from utils.readExcel import ReadData
from basetest import BaseTest

#This test case is to verify the publish posts function
class TestPostBlog(BaseTest):

    @pytest.mark.smoke
    def test_post_blog(self, setup, base_test):
        self.driver = setup
        self.blog_posts = BlogPosts(self.driver)
        self.blog_publish = BlogPublish(self.driver)
        self.my_site = MySite(self.driver)

        current_time = self.driver.device_time
        self.tc_sheet = 'post_blog'
        self.exp_addTitle = ReadData.readData(self.filepath, self.tc_sheet, 2, 1) + current_time
        self.exp_blogtext = ReadData.readData(self.filepath, self.tc_sheet, 2, 2) + current_time

        # login function
        self.login_action.login_steps(self.email, self.password)

        # Navigate to blog page
        self.my_site.click_posts()
        self.blog_posts.click_addnew()
        self.blog_posts.click_addblog()

        # write post
        self.blog_publish.text_blog_title(self.exp_addTitle)
        self.blog_publish.text_blog_text(self.exp_blogtext)
        sleep(2)

        # publish
        self.blog_publish.click_publish()
        self.blog_publish.click_publishnow()

        # validate confirmation message
        actual_msg = self.blog_publish.get_confirm_msg()
        if actual_msg == 'Post published':
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 3, "Pass")
            self.driver.back()
            self.logout_action.logout_steps()
            assert True
        else:
            ReadData.writeData(self.filepath, self.tc_sheet, 2, 3, "Fail")
            self.driver.back()
            self.logout_action.logout_steps()
            assert False
