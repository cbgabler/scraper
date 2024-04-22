from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from user_agents import user_agents
import random
import csv
import constants as cts
import os

def init_driver():
    ## collect random user agent to mask browser
    random_user_agent = random.choice(user_agents)
    ## initiate options through uc chrome
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument(f"user-agent={random_user_agent}")
    driver = uc.Chrome(options=options)
    return driver

def dk_extract_data(dk_urls, driver):
    # Create the folder if it doesn't exist
    if not os.path.exists("sport_csvs"):
        os.makedirs("sport_csvs")

    for sport, url in dk_urls.items():
        print(f"Now extracting DraftKings {sport}")
        driver.get(url)
        wait = WebDriverWait(driver, 5)  # Adjust the timeout as needed
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, cts.DraftKingsConstants.MAIN_DIV)))
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        divs = soup.find_all("div", class_=cts.DraftKingsConstants.MAIN_DIV)

        game_day_data = {}
        for div in divs:
            date_div = div.find("div", class_="sportsbook-table-header__title")
            if date_div:
                date_text = date_div.text.strip().lower()
                print(f"{sport} {date_text}")
                game_day_data[date_text] = div

        parsed_data = {}
        for date, html in game_day_data.items():
            mlb_team = html.findAll(cts.DraftKingsConstants.TEAM_TYPE, class_=cts.DraftKingsConstants.TEAM_HTML)
            mlb_ml = html.findAll(cts.DraftKingsConstants.ML_TYPE, class_=cts.DraftKingsConstants.ML_HTML)
            parsed_data[date] = []  # Initialize an empty list for each date
            print(mlb_team, mlb_ml)
            for team, ml in zip(mlb_team, mlb_ml):
                parsed_data[date].append([team.text.strip(), ml.text.strip()])
        
        print(parsed_data)

        for date, arr_info in parsed_data.items():
            with open(os.path.join("sport_csvs", f"DraftKings_{sport}_{date}.csv"), mode='w', newline='') as today_file:
                fieldnames = ["Team", "Moneyline"]
                writer = csv.DictWriter(today_file, fieldnames=fieldnames)
                writer.writeheader()
                for team_info in arr_info:
                    writer.writerow({"Team": team_info[0], "Moneyline": team_info[1]})

