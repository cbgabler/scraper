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
import csv

def instantiate_driver():
    ## collect random user agent to mask browser
    random_user_agent = random.choice(user_agents)
    ## initiate options through uc chrome
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument(f"user-agent={random_user_agent}")
    driver = uc.Chrome(options=options)
    return driver

def start_driver(player_url, driver):
    driver.get(player_url)
    time.sleep(5)
    page = driver.page_source
    driver.quit()
    return page

def extract_dk(dk_html):
    ## use instantiated driver for internal chrome parsing

    soup = BeautifulSoup(dk_html, 'lxml')

    container = soup.find_all("span", attrs={"class" : "sportsbook-odds american no-margin default-color"})
    
    with open("output", mode='w', newline='') as file:
        writer = csv.writer(file)
        for span in container:
            writer.writerow([span.text.strip()])
    # clean_html = cleanup(player_url, player)
