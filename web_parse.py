import requests
import config
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import csv
from seleniumwire import webdriver
import undetected_chromedriver as uc
from user_agents import user_agents
import random
from cleanup import cleanup

def start_driver():
    random_user_agent = random.choice(user_agents)
    print(random_user_agent)
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={random_user_agent}")
    driver = uc.Chrome(options=options)
    return driver

def extract_points(player_url, driver):
    driver.get(player_url)
    print(driver.page_source)
    player_html = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    player = player_html.title.string
    clean_html = cleanup(player_url, player)
    return clean_html