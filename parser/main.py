import web_parse as wp
import config
import constants as cts
import timeit

def main():
    # Measure time taken to execute extract_data
    start_time = timeit.default_timer()
    driver = wp.init_driver()
    db = wp.init_mongo()
    dk_urls = config.dk_url_creator(cts.DraftKingsConstants.DEFAULT_URL, cts.LEAGUES)
    betus_urls = config.betus_url_creator(cts.BetUSConstants.DEFAULT_URL, cts.LEAGUES)
    b365_urls = config.b365_url_creator(cts.B365Constants.DEFAULT_URL,  cts.B365)
    print(dk_urls)
    wp.dk_extract_data(dk_urls, driver, db)
    ## wp.ggbet_extract_data(driver)
    ## wp.extract_MGM(driver)
    ## wp.b365_extract_data(b365_urls, driver)
    ## wp.betus_extract_data(betus_urls, driver)
    end_time = timeit.default_timer()
    
    print(f"Time taken: {end_time - start_time} seconds")
    driver.quit()

if __name__ == '__main__':
    main()