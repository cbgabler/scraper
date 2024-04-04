import api_data as ad
import web_parse as wp
import config
import constants as cts
import webbrowser as wb
from bs4 import BeautifulSoup
import timeit

def main():
    # Measure time taken to execute extract_points
    start_time = timeit.default_timer()
    driver = wp.start_driver()
    player_url = config.url_creator(cts.DEFAULT_URL, cts.PLAYER_NUM)
    wp.extract_points(player_url, driver)
    end_time = timeit.default_timer()
    
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()