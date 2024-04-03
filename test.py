from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_headers import Headers
import undetected_chromedriver as uc
import webbrowser as wb


driver = uc.Chrome(seleniumwire_options={})

def create_header():
    header = Headers().generate()
    return header

def request_interceptor(request):
    del request.headers["user-agent"]
    request.headers

driver.request_interceptor = request_interceptor



import api_data as ad
import web_parse as wp
import config
import constants as cts
import webbrowser as wb
import time
import headers

def main():
    driver = wp.start_driver()
    player_url = config.url_creator(cts.DEFAULT_URL, cts.PLAYER_NUM)
    print(player_url)
    ml_prop = wp.extract_points(player_url, driver)
    if (ml_prop):
        print(ml_prop)
    else:
        print("nope!")
    driver.quit()
    time.sleep(3)



if __name__ == '__main__':
    main()
