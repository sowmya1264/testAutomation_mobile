from pages.email_form import EmailForm
from pages.launch_page import LaunchPage
from pages.login_form import LoginForm
from pages.site_selection import SiteSelection
from utils.log_gen import LogGen


class LoginActions:

    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.log_gen()
        self.email_form = EmailForm(self.driver)
        self.login_form = LoginForm(self.driver)
        self.site_selection = SiteSelection(self.driver)
        self.launch_page = LaunchPage(self.driver)

    def login_steps(self, email, password):

        self.launch_page.click_continue_button()
        self.email_form.text_email_id(email)
        self.email_form.click_continue_button()
        self.login_form.text_pwd(password)
        self.login_form.click_continue_button()
        self.site_selection.click_done_button()




