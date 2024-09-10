from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Main Menu button')
def click_main_menu(context):
    context.app.main_page.click_main_menu()
    sleep(5)


@when('Click on “Connect the company')
def click_connect_the_company(context):
    context.app.main_page.click_connect_the_company()
    sleep(12)
