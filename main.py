import api_data as ad
import web_parse as wp
import config
import constants as cts
import webbrowser as wb
from bs4 import BeautifulSoup

def main():
    driver = wp.start_driver()
    html = wp.extract_points("https://www.basketball-reference.com/players/t/tatumja01.html", driver)
    print(html)
    return 0

if __name__ == '__main__':
    main()