from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from user_agents import user_agents
import random
import csv
import constants as cts
import os
import webbrowser
import time
import pymongo
import datetime
from dotenv import load_dotenv

load_dotenv()

def init_mongo():
    mongo_uri = os.getenv("CONNECTION_STR")
    if not mongo_uri:
        raise ValueError("MONGO_URI is not set in the .env file")
    client = pymongo.MongoClient(mongo_uri)
    db = client["scrapedLines"]
    return db

def init_driver():
    random_user_agent = random.choice(user_agents)

    options = Options()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={random_user_agent}")
    driver = webdriver.Chrome(options=options)
    
    return driver

def dk_extract_data(dk_urls, driver, db):
    print(f"Now extracting DraftKings Basketball")
    driver.get(dk_urls)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, cts.DraftKingsConstants.MAIN_DIV)))
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all("div", class_=cts.DraftKingsConstants.MAIN_DIV)

    game_day_data = {}
    for div in divs:
        date_div = div.find("div", class_="sportsbook-table-header__title")
        if date_div:
            date_text = date_div.text.strip().lower()
            game_day_data[date_text] = div

    parsed_data = parse_data(game_day_data, cts.DraftKingsConstants.TEAM_TYPE, cts.DraftKingsConstants.TEAM_HTML,
                            cts.DraftKingsConstants.ML_TYPE, cts.DraftKingsConstants.ML_HTML)
    write_data(parsed_data, "basketball", "dk", db)

def betus_extract_data(betus_urls, driver):
    for sport, url in betus_urls.items():
        driver.set_window_size(1080, 800)
        print(f"Now extracting BetUS {sport}")
        driver.get(url)
        webbrowser.open(url)
        time.sleep(5)
        html = driver.page_source

        with open(f"betus_{sport}_data.html", "w", encoding="utf-8") as file:
            file.write(html)
        
        soup = BeautifulSoup(html, "lxml")
        divs = soup.find_all("div", class_=cts.BetUSConstants.MAIN_DIV)

        game_day_data = {}
        for div in divs:
            date_div = "today"
            if date_div:
                game_day_data[date_div] = div

        parsed_data = parse_data(game_day_data, cts.BetUSConstants.TEAM_TYPE, cts.BetUSConstants.TEAM_HTML,
                                    cts.BetUSConstants.ML_TYPE, cts.BetUSConstants.ML_HTML)
        write_data(parsed_data, sport, "betus")

def b365_extract_data(b365_urls, driver):
    for sport, url in b365_urls.items():
        print(f"Now extracting B365 {sport}")
        driver.get(url)
        wait = WebDriverWait(driver, 100)  # Adjust the timeout as needed
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, cts.B365Constants.MAIN_DIV)))
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        divs = soup.find_all("div", class_=cts.B365Constants.MAIN_DIV)

        game_day_data = {}
        for div in divs:
            date_div = div.find("div", class_="scb-rcl-MarketHeaderLabel rcl-MarketHeaderLabel-isdate ")
            if date_div:
                date_text = date_div.text.strip().lower()
                game_day_data[date_text] = div
        print(game_day_data)

        # Get the appropriate team HTML and ML HTML class names based on the sport from constants
        team_html_class = cts.B365Constants.TEAM_HTML.get(sport.lower())
        ml_html_class = cts.B365Constants.ML_HTML.get(sport.lower())
        if team_html_class is None or ml_html_class is None:
            print(f"No HTML class found for {sport}. Skipping extraction.")
            continue

        # Extract data using the correct team HTML and ML HTML class names
        parsed_data = parse_data(game_day_data, cts.B365Constants.TEAM_TYPE, team_html_class,
                                  cts.B365Constants.ML_TYPE, ml_html_class)
        append_data(parsed_data, sport, "b365")


def ggbet_extract_data(driver):
    print(f"Now extracting GGBET basketball")
    driver.get("https://ggbet.com/en/sports/tournament/nba-24-10")
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all("a", class_="__app-SmartLink-link overviewRow__container___2uPYc")

    game_day_data = {}
    for div in divs:
        date_div = div.find("div", class_="fixtureData__text___1JMWR")
        print(date_div)
        if date_div:
            date_text = date_div.text.strip().lower()
            print(date_text)
            game_day_data[date_text] = div

    parsed_data = parse_data(game_day_data, "div", "__app-LogoTitle-name logoTitle__name___3_ywM",
                                    "div", "oddButton__coef___2tokv")
    write_data(parsed_data, "basketball", "GGBET")

def extract_MGM(driver):
    print("Now extracting MGMGrand Football")
    driver.get("https://sports.az.betmgm.com/en/sports/football-11")
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all("ms-widget-layout", class_="row sport-lobby widget-layout")

    headers = soup.find_all("div", class_="grid-group-header ng-star-inserted")

    game_day_data = {}
    for div in divs:
        date_div = soup.find("div", class_="event-info-container ng-star-inserted")
        print(date_div)
        if date_div:
            date_text = date_div.text.strip().lower()
            game_day_data[date_text] = div

    header_data = []
    for header in headers:
        header_data.append(header.text.strip().lower())

    print(header_data)

    parsed_data = parse_data(game_day_data, cts.MGMConstants.TEAM_TYPE, cts.MGMConstants.TEAM_HTML,
                                    cts.MGMConstants.ML_TYPE, cts.MGMConstants.ML_HTML)
    write_data(parsed_data, "football", "MGMGrand")

def write_data(parsed_data, sport, book, db):
    collection = db["draftkings"]
    for date, arr_info in parsed_data.items():
        for team_info in arr_info:
            document = {
                "date": date,
                "team": team_info[0],
                "moneyline": team_info[1],
                "sport": sport,
                "book": book
            }
            print(document)
            collection.insert_one(document)  # Insert the document into MongoDB

def append_data(parsed_data, sport, book, db):
    collection = db[book]
    for date, arr_info in parsed_data.items():
        for team_info in arr_info:
            existing_document = collection.find_one({"team": team_info[0], "date": date, "sport": sport, "book": book})
            if existing_document:
                collection.update_one(
                    {"_id": existing_document["_id"]},
                    {"$set": {"moneyline": team_info[1]}}
                )
            else:
                document = {
                    "date": date,
                    "team": team_info[0],
                    "moneyline": team_info[1],
                    "sport": sport,
                    "book": book
                }
                collection.insert_one(document)

def parse_data(game_day_data, team_type, team_html, ml_type, ml_html):
    parsed_data = {}
    for date, html in game_day_data.items():
        mlb_team = html.findAll(team_type, team_html)
        mlb_ml = html.findAll(ml_type, ml_html)
        parsed_data[date] = []  # Initialize an empty list for each date
        for team, ml in zip(mlb_team, mlb_ml):
            parsed_data[date].append([team.text.strip(), ml.text.strip()])
    print(parsed_data)
    return parsed_data

def normalize_data(val):
    normalized_line = val
    if normalized_line <= 0:
        normalized_line = -100/(normalized_line - 1)
    else:
        normalized_line = (normalized_line - 1) * 100
    return normalized_line
