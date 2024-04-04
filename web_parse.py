import requests
import config
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from user_agents import user_agents
import random
from cleanup import cleanup
import time

def start_driver():
    ## collect random user agent to mask browser
    random_user_agent = random.choice(user_agents)
    print(random_user_agent)

    ## initiate options through uc chrome
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument(f"user-agent={random_user_agent}")
    driver = uc.Chrome(options=options)
    return driver

def extract_points(player_url, driver):
    ## use instantiated driver for internal chrome parsing
    driver.get(player_url)
    time.sleep(5)
    page = driver.page_source
    driver.quit()

    with open('page_source.html', 'w', encoding='utf-8') as file:
        file.write(page)

    soup = BeautifulSoup(page, 'html.parser')

    container = soup.find_all("span", attrs={"class" : "sc-d392def8-0 hkPGsE"})
    print(container)
    # clean_html = cleanup(player_url, player)