import unittest
import constants as cts
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import web_parse as wp
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

def test_clicking(driver, db):
    i = 1
    while i <= 15:
        action = ActionChains(driver)
        driver.get("https://sportsbook.draftkings.com/")
        driver.find_element(By.XPATH, f"//*[@id='root']/section/section[2]/div[1]/div[1]/div[2]/ul/li[{i}]/a").click()
        print(driver.current_url)
        ## popular_clickables = popular.find_elements(By.CLASS_NAME, "sportsbook-navitation-item-title-text")
        ## popular_clickables[i].click()
        sub_clickables = driver.find_elements(By.CLASS_NAME, "sportsbook-category-tab-name")
        for j, sub_clickable in enumerate(sub_clickables):
            if j == 13:
                break
            if j == 1:
                print(1)
                continue
            print(sub_clickable)
            action.move_to_element(sub_clickable).click().perform()
            sub_url = driver.current_url
            dk_extract_data(sub_url, driver, db)
        url = driver.current_url
        print(url)
        i += 1

def dk_extract_data(url, driver, db):
    driver.get(url)
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

    parsed_data = wp.parse_data(game_day_data, cts.DraftKingsConstants.TEAM_TYPE, cts.DraftKingsConstants.TEAM_HTML,
                                cts.DraftKingsConstants.ML_TYPE, cts.DraftKingsConstants.ML_HTML)
    wp.write_data(parsed_data, "football", "dk", db)

def clicking_b365(driver):
    action = ActionChains(driver)
    driver.get("https://www.co.bet365.com/?_h=7zGwoPT5idsD__-vUHcGpw%3D%3D&btsffd=1#/HO/")

if __name__ == '__main__':
    unittest.main()
