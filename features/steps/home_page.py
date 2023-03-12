from time import sleep
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import *
from url_list import *
from test_data import *
from environment import *

CHATS_ICON = "//a[@aria-label = 'Chats']"

@then('User should land on application home page')
def is_user_on_home_page(context):
    visibility(context, CHATS_ICON)