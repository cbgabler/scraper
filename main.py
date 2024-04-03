import api_data as ad
import web_parse as wp
import config
import constants as cts
import webbrowser as wb
import time
import headers
from bs4 import BeautifulSoup

def main():
    driver = wp.start_driver()
    driver.get("https://www.basketball-reference.com/players/t/tatumja01.html")

    time.sleep(5)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")

    print(soup)

    # Close the WebDriver session
    driver.quit()

if __name__ == '__main__':
    main()