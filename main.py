import web_parse as wp
import config
import constants as cts
import timeit

def main():
    # Measure time taken to execute extract_data
    start_time = timeit.default_timer()
    driver = wp.init_driver()
    dk_urls = config.dk_url_creator(cts.DraftKingsConstants.DEFAULT_URL, cts.SPORTS)
    b365_urls = config.b365_url_creator(cts.B365Constants.DEFAULT_URL, cts.B365)
    print(b365_urls)
    
    wp.b365_extract_data(b365_urls, driver)
    end_time = timeit.default_timer()
    
    print(f"Time taken: {end_time - start_time} seconds")
    driver.quit()

if __name__ == '__main__':
    main()