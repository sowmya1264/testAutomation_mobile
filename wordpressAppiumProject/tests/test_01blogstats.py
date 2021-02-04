from time import sleep
import pytest
from pages.blog_posts import BlogPosts
from pages.blog_publish import BlogPublish
from pages.my_site import MySite
from pages.stats_page import StatsPage
from basetest import BaseTest

# This test case is to verify if the posts count displayed in the Stats page is correct and is matching with the Blogs page
class TestBlogStats(BaseTest):

    @pytest.mark.regression
    def test_blog_stats(self, setup, base_test):
        self.driver = setup
        self.blog_posts = BlogPosts(self.driver)
        self.blog_publish = BlogPublish(self.driver)
        self.my_site = MySite(self.driver)
        self.stats = StatsPage(self.driver)

        # login function
        self.login_action.login_steps(self.email, self.password)
        self.logger.info("*** Login Successful***")

        # Navigate to blog page
        self.my_site.click_posts()
        self.logger.info("*** Navigated to blogs page ***")

        # Count number of blogs posted
        blog_count = 0
        blog_titles = []
        end_of_page = False
        while not end_of_page:
            title_ele = self.blog_posts.click_blogtitle()
            print(title_ele)
            for i in title_ele:
                if i not in blog_titles:
                    blog_count += 1
                    blog_titles.append(i)
            end_of_page = self.blog_posts.displayed_endofpage()
            if end_of_page:
                self.logger.info("***end of page reached***")
                self.logger.info(f"Total blogs displayed under Published tab={blog_count}")
                break
            else:
                self.driver.swipe(794, 1630, 794, 1000, 300)
                self.logger.info("***scrolled the page***")
                continue
        self.logger.info(f"Blog titles{blog_titles}")

        # navigate back to my site page
        self.driver.back()

        # Stats
        self.my_site.click_stats()
        self.logger.info("***Navigated to Stats page***")
        sleep(5)
        self.driver.swipe(794, 1630, 794, 50, 500)
        sleep(5)
        stats_posts_count = int(self.stats.get_stats_posts())
        print(f"Blogs in stats page = {stats_posts_count}")
        self.logger.info(f"Blogs in stats page = {stats_posts_count}")

        # validate stats count against blogs
        if blog_count == stats_posts_count:
            self.driver.back()
            self.logout_action.logout_steps()
            self.logger.info("*******logout successful ******")
            self.logger.info(f"blogs count {blog_count} matches with stats posts count {stats_posts_count}")
            assert True

        else:
            self.driver.back()
            self.logout_action.logout_steps()
            self.logger.info("*******logout successful ******")
            self.logger.info(f"blogs count {blog_count} does not match with stats posts count {stats_posts_count}")
            assert False
