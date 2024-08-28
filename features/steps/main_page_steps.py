from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when('Click on “Connect the company')
def click_connect_the_company(context):
    context.app.main_page.click_connect_the_company()

sleep(10)