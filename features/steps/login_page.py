from time import sleep
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import *
from url_list import *
from selenium.webdriver.chrome.options import Options
from environment import *

COOKIE_BANNER_TITLE_TXT = "//div[@id = 'consent_cookies_title']"
ONLY_ESSENTIAL_COOKIES_BTN = "//button[@data-cookiebanner = 'accept_only_essential_button']"
EMAIL_INPUT_FLD = "//input[@id = 'email']"
PASSWORD_INPUT_FLD = "//input[@id = 'pass']"
LOGIN_BTN = "//button[@id = 'loginbutton']"

@given('User start at login page')
def open_login_page(context):
    open_page(context, login_page_url)

@then('User is able to see cookies information banner')
def cookies_banner_present(context):
    visibility(context, COOKIE_BANNER_TITLE_TXT)