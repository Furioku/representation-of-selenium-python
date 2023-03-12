from time import sleep
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import *
from url_list import *
from test_data import *
from environment import *

COOKIE_BANNER_TITLE_TXT = "//div[@id = 'consent_cookies_title']"
ONLY_ESSENTIAL_COOKIES_BTN = "//button[@data-cookiebanner = 'accept_only_essential_button']"
EMAIL_INPUT_FLD = "//input[@id = 'email']"
PASSWORD_INPUT_FLD = "//input[@id = 'pass']"
LOGIN_BTN = "//button[@id = 'loginbutton']"

@given('User start at login page')
def open_login_page(context):
    open_page(context, login_page_url)

@then('User is able to see cookies information banner and verify text in title banner')
def cookies_banner_present(context):
    visibility(context, COOKIE_BANNER_TITLE_TXT)
    text_from_cookies_banner_title = context.driver.find_element(By.XPATH, COOKIE_BANNER_TITLE_TXT).text
    assert str(text_from_cookies_banner_title) == TEXT_IN_COOKIES_BANNER_TITLE

@when('User press Only Allow Essential Cookies button')
def press_on_allow_essential_btn(context):
    click(context, ONLY_ESSENTIAL_COOKIES_BTN)
    

@then('User is able to see email and password input fields')
def visibility_of_pass_and_email_fields(context):
    visibility(context, EMAIL_INPUT_FLD)
    visibility(context, PASSWORD_INPUT_FLD)

@when('User type proper {email} into email input field')
def type_in_email(context, email):
    type(context, EMAIL_INPUT_FLD, email)

@when('User type proper {password} into password input field')
def type_in_password(context, password):
    type(context, PASSWORD_INPUT_FLD, password)

@when('User click on Logg inn button')
def click_on_login_btn(context):
    click(context, LOGIN_BTN)