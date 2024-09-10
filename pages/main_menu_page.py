from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait


class MainMenuPage(Page):
    CLICK_USER_ICON = (By.CSS_SELECTOR, "[class='menu-img-agent-listing']")

    def click_user_icon(self):
        self.wait_and_click(*self.CLICK_USER_ICON)
