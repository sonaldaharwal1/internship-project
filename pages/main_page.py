from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class MainPage(Page):
    # CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, "[class='button-link-menu w-inline-block']")
    CONNECT_THE_COMPANY_BTN = (By.XPATH, "//a[contains(@href, '/book-presentation')]")
    CLICK_MAIN_MENU_BUTTON = (By.CSS_SELECTOR, "[class='circle-gradient']")

    def click_main_menu(self):
        self.wait_and_click(*self.CLICK_MAIN_MENU_BUTTON)

    def  click_connect_the_company(self):
        element = self.find_elements(*self.CONNECT_THE_COMPANY_BTN)
        element[1].click()
        sleep(6)
        #self.wait_and_click(*self.CONNECT_THE_COMPANY_BTN)

