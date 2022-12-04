from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from random import randrange
from datetime import timedelta
from datetime import datetime
import glob
import pandas as pd

d = 0

def create_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(120)
    return driver

def get_data(driver):
    driver.get("https://opensea.io/collection/lostminers")
    sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/div/div/div[5]/div/div[3]/div[3]/div[3]/div[3]/div/div[1]").click()
    sleep(5)
    print(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/main/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div/ul/li[2]/div[5]/div/div/a").click()
    sleep(5)


get_data(create_driver())

# import requests 
# from bs4 import BeautifulSoup


# page = requests.get('https://opensea.io/cartoon_head')
# bs = BeautifulSoup(page.content, features='lxml')
# for link in bs.findAll('a'):
#     print(link.get('href'))