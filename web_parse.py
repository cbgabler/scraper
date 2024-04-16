from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import undetected_chromedriver as uc
from user_agents import user_agents
import random
import time
import csv
import constants as cts

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

def extract_data(bookie_urls, driver):
    for bookie, url in bookie_urls.items():
        print(f"Now extracting{bookie}")
        driver.get(url)
        html = driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(html, "lxml")
        divs = soup.find_all("div", class_=cts.MAIN_DIV[bookie])

        today_games = []
        tomorrow_games = []
        for div in divs:
            date_div = div.find("div", class_="sportsbook-table-header__title")
            if date_div:
                date_text = date_div.text.strip().lower()
                if "today" in date_text:
                    today_games.append(div)
                elif "tomorrow" in date_text:
                    tomorrow_games.append(div)

        today_data = {}
        for game in today_games:
            mlb_team = game.findAll(cts.TEAM_TYPE[bookie], class_=cts.TEAM_HTML[bookie])
            mlb_ml = game.findAll(cts.ML_TYPE[bookie], class_=cts.ML_HTML[bookie])

            for team, ml in zip(mlb_team, mlb_ml):
                today_data[team.text.strip()] = ml.text.strip()

        tomorrow_data = {}
        for game in tomorrow_games:
            mlb_team = game.findAll(cts.TEAM_TYPE[bookie], class_=cts.TEAM_HTML[bookie])
            mlb_ml = game.findAll(cts.ML_TYPE[bookie], class_=cts.ML_HTML[bookie])

            for team, ml in zip(mlb_team, mlb_ml):
                tomorrow_data[team.text.strip()] = ml.text.strip()

        with open(f"{bookie}_today_games.csv", mode='w', newline='') as today_file:
            fieldnames = ["Team", "Moneyline"]
            writer = csv.DictWriter(today_file, fieldnames=fieldnames)
            writer.writeheader()
            for team, moneyline in today_data.items():
                writer.writerow({"Team": team, "Moneyline": moneyline})

        with open(f"{bookie}_tomorrow_games.csv", mode='w', newline='') as tomorrow_file:
            fieldnames = ["Team", "Moneyline"]
            writer = csv.DictWriter(tomorrow_file, fieldnames=fieldnames)
            writer.writeheader()
            for team, moneyline in tomorrow_data.items():
                writer.writerow({"Team": team, "Moneyline": moneyline})

