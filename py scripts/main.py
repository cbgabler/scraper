import api_data as ad
##import web_parse as wp
import config
import constants as cts
import webbrowser as wb
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'
}

def start_driver():
    ## bs4 from BeautifulSoup does not work with SofaScore
    ## using selenium (thank you to https://github.com/danielsaban/data-scraping-sofascore/blob/master/html_parser.py)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(executable_path=r'./chromedriver', options=chrome_options)

def main():
    player_url = config.url_creator(cts.DEFAULT_URL, cts.PLAYER_NUM)
    wb.open(player_url, new = 0)
    player_data = {}
    

if __name__ == '__main__':
    main()