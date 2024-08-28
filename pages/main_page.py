from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait

class MainPage(Page):

    CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, "[class='button-link-menu w-inline-block']")


    def click_connect_the_company(self):
        self.click(*self.CONNECT_THE_COMPANY_BTN )

