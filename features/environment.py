from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from url_list import *

CHROMEDRIVER_PATH = "C:/Users/phili/representation-of-selenium-python/chromedriver.exe"

def after_scenario(context, scenario):
    context.driver.quit()    

def open_page(context, env_url):
    context.driver = create_driver()
    context.driver.get(env_url)
    context.driver.maximize_window()

def create_driver():
    options = Options()
    #comment 2 lines below to open browser in visible state
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("lang=en-GB")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(chrome_options = options)
    return driver
