from time import sleep
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver

def invisibility(context, xpath):
    WebDriverWait(context.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, xpath)))

def visibility(context, xpath):
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def visibilityCSS(context, css):
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def presence(context, xpath):
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))

def presenceCSS(context, css):
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

def url_check(context, url):
    WebDriverWait(context.driver, 20).until(EC.url_to_be(url))

def type(context, xpath, text):
    context.driver.find_element(By.XPATH, xpath).send_keys(text)

def send_keys(context, xpath, keys):
    context.driver.find_element(By.XPATH, xpath).send_keys(keys)

def click(context, xpath):
    context.driver.find_element(By.XPATH, xpath).click()

def clickCSS(context, css):
    context.driver.find_element(By.CSS_SELECTOR, css).click()

