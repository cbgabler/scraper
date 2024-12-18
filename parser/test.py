import unittest
import constants as cts
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_clicking(driver):
    action = ActionChains(driver)
    driver.get("https://sportsbook.draftkings.com/")
    popular = driver.find_element(By.CLASS_NAME, "sportsbook-expandable-shell__wrapper")
    popular_clickables = popular.find_elements(By.CLASS_NAME, "sportsbook-navitation-item-title-text")
    for clickable in popular_clickables:
        clickable.click()
        driver.get(driver.current_url)
        sub_clickables = driver.find_elements(By.CLASS_NAME, "sportsbook-category-tab-name")
        for i, sub_clickable in enumerate(sub_clickables):
            sub_url = driver.current_url
            if i == 13:
                break
            if i == 1:
                print(1)
                continue
            print(sub_clickable)
            action.move_to_element(sub_clickable).click().perform()
            print(sub_url)
        url = driver.current_url
        print(url)


if __name__ == '__main__':
    unittest.main()