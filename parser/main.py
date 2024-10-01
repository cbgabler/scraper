import web_parse as wp
import config
import constants as cts
import timeit

def main():
    # Measure time taken to execute extract_data
    start_time = timeit.default_timer()
    driver = wp.init_driver()
    dk_urls = config.dk_url_creator(cts.DraftKingsConstants.DEFAULT_URL, cts.LEAGUES)
    betus_urls = config.betus_url_creator(cts.BetUSConstants.DEFAULT_URL, cts.LEAGUES)
    print(betus_urls)
    wp.dk_extract_data(dk_urls, driver)
    wp.ggbet_extract_data(driver)
    ## wp.betus_extract_data(betus_urls, driver)
    end_time = timeit.default_timer()
    
    print(f"Time taken: {end_time - start_time} seconds")
    driver.quit()

if __name__ == '__main__':
    main()