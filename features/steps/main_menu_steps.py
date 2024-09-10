from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Click on User Icon')
def click_on_user_icon(context):
    context.app.main_menu_page.click_user_icon()
    sleep(6)