from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Switch the new tab')
def switch_window(context):
    context.app.main_page.switch_to_new_window()

@then('Verify the right tab opens')
def verify_Connect_page_opened(context):
    context.app.connect_the_company_page.verify_Connect_page_url()

    sleep(5)

