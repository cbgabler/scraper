import unittest
import constants as cts
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import web_parse as wp
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

def test_clicking(driver, db):
    i = 1
    while i <= 14:
        action = ActionChains(driver)
        driver.get("https://sportsbook.draftkings.com/")
        driver.find_element(By.XPATH, f"//*[@id='root']/section/section[2]/div[1]/div[1]/div[2]/ul/li[{i}]/a").click()
        print(driver.current_url)
        driver.get(driver.current_url)
        ## popular_clickables = popular.find_elements(By.CLASS_NAME, "sportsbook-navitation-item-title-text")
        ## popular_clickables[i].click()
        f = 0
        print(driver.find_elements(By.CLASS_NAME, "sportsbook-category-tab-name"))
        print(len(driver.find_elements(By.CLASS_NAME, "sportsbook-category-tab-name")))
        while f < len(driver.find_elements(By.CLASS_NAME, "sportsbook-category-tab-name")):
            driver.get(driver.current_url)
            sub_clickable = driver.find_elements(By.XPATH, "//*[@id='root']/section/section[2]/section/div[4]/div/div[1]/div[1]/div")
            print(sub_clickable)
            action.move_to_element(sub_clickable[f]).click().perform()
            sub_url = driver.current_url
            print(sub_url)
            extract_pass(sub_url, driver, db)
            f += 1
        url = driver.current_url
        print(url)
        i += 1

def dk_extract_data(url, driver, db):
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "side-rail-name")))
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all("a", class_="side-rail-name-link")

    game_day_data = {}
    for div in divs:
        date_div = div.find("div", class_="sportsbook-table-header__title")
        if date_div:
            date_text = date_div.text.strip().lower()
            game_day_data[date_text] = div

    parsed_data = wp.parse_data(game_day_data, cts.DraftKingsConstants.TEAM_TYPE, cts.DraftKingsConstants.TEAM_HTML,
                                cts.DraftKingsConstants.ML_TYPE, cts.DraftKingsConstants.ML_HTML)
    wp.write_data(parsed_data, "football", "dk", db)

def extract_pass(url, driver, db):
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "side-rail-name")))
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all("a", class_="side-rail-name-link")
    odds = soup.find_all("span", class_="sb-selection-picker__selection-odds")
    amounts = soup.find_all("span", class_="sb-selection-picker__selection-label")

    for i, div in enumerate(divs):
        name = div.text
        odd = odds[i].text
        amount = amounts[i].text
        write_data(name, amount, odd, "football", "dk", "passyards", db)

def write_data(name, amount, odd, sport, book, db_name, db):
    collection = db[f"{db_name}"]
    document = {
        "name": name,
        "amount": amount,
        "odd": odd,
        "sport": sport,
        "book": book
    }
    print(document)
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

def clicking_b365(driver):
    action = ActionChains(driver)
    driver.get("https://www.co.bet365.com/?_h=7zGwoPT5idsD__-vUHcGpw%3D%3D&btsffd=1#/HO/")


if __name__ == '__main__':
    unittest.main()
