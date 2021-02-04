from pages.basepage import BasePage


class BlogPosts(BasePage):
    addnew = '//android.widget.ImageButton[@content-desc="Create a post or story"]'
    addblog = '//android.widget.TextView[@text="Blog post"]'
    blogtitle = 'title'
    endofpage = 'endlist_indicator'

    def click_addnew(self):
        self.page_utils.wait_element_click('xpath', self.addnew)
        self.driver.hide_keyboard()

    def click_addblog(self):
        self.page_utils.wait_element_click('xpath', self.addblog)
        self.driver.hide_keyboard()

    def click_blogtitle(self):
        elements = self.page_utils.wait_elements_click('id', self.blogtitle)
        return elements

    def displayed_endofpage(self):
        element_displayed = self.page_utils.wait_element_isdisplayed('id', self.endofpage)
        return element_displayed
