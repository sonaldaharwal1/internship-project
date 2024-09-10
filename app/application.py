from pages.main_page import MainPage
from pages.base_page import Page
from pages.login_page import Login
from pages.connect_the_company_page import Connect
from pages.main_menu_page import MainMenuPage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.main_page = MainPage(driver)

        self.login_page = Login(driver)

        self.connect_the_company_page = Connect(driver)

        self.main_menu_page = MainMenuPage(driver)