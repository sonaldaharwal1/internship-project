from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given ('Open the singin page')
def open_Reelly(context):
  context.app.login_page.open()


@when('Log in to the page')
def click_login(context):

  context.app.login_page.login()

