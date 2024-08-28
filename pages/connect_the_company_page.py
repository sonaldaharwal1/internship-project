from selenium.webdriver.common.by import By

from pages.base_page import Page

class Connect(Page):
    def verify_Connect_page_url(self):
        self.verify_partial_url('https://soft.reelly.io/book-presentation')