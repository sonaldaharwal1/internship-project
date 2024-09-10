from selenium.webdriver.common.by import By

from pages.base_page import Page


class Login(Page):
    CONTINUE_BTN = (By.CSS_SELECTOR, "[class='login-button w-button']")
    EMAIL_FEILD = (By.CSS_SELECTOR, '#email-2')
    PWD_FIELD = (By.CSS_SELECTOR, '#field')

    def open(self):
        self.open_url('https://soft.reelly.io/sign-in')

    # i remove my username and password, please put username and password for reviewing the code
    def login(self):
        self.input_text('username', *self.EMAIL_FEILD)
        self.input_text('Password', *self.PWD_FIELD)
        self.wait_and_click(*self.CONTINUE_BTN)
