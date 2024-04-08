from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import undetected_chromedriver as uc
from user_agents import user_agents
import random
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

def start_driver(player_urls, driver):
    driver.get(player_urls)
    time.sleep(2)
    page = driver.page_source
    return page

def extract_dk(dk_html):
    soup = BeautifulSoup(dk_html, "lxml")

    # Find all instances of "parlay-card-10-a"
    divs = soup.find_all("div", class_="parlay-card-10-a")

    # Loop through each div to separate today's and tomorrow's games
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

    # Process today's games
    today_data = {}
    for game in today_games:
        mlb_team = game.findAll("div", class_="event-cell__name-text")
        mlb_ml = game.findAll("span", class_="sportsbook-odds american no-margin default-color")

        for team, ml in zip(mlb_team, mlb_ml):
            today_data[team.text.strip()] = {"moneyline": ml.text.strip()}

    # Process tomorrow's games
    tomorrow_data = {}
    for game in tomorrow_games:
        mlb_team = game.findAll("div", class_="event-cell__name-text")
        mlb_ml = game.findAll("span", class_="sportsbook-odds american no-margin default-color")

        for team, ml in zip(mlb_team, mlb_ml):
            tomorrow_data[team.text.strip()] = ml.text.strip()

    # Example: write the information to separate CSV files for today and tomorrow
    with open("today_games.csv", mode='w', newline='') as today_file:
        fieldnames = ["Team", "Odds"]
        writer = csv.DictWriter(today_file, fieldnames=fieldnames)
        writer.writeheader()
        for team, odds in today_data.items():
            writer.writerow({"Team": team, "Odds": odds})

    with open("tomorrow_games.csv", mode='w', newline='') as tomorrow_file:
        fieldnames = ["Team", "Odds"]
        writer = csv.DictWriter(tomorrow_file, fieldnames=fieldnames)
        writer.writeheader()
        for team, odds in tomorrow_data.items():
            writer.writerow({"Team": team, "Odds": odds})
