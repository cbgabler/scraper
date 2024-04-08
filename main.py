import web_parse as wp
import config
import constants as cts
import timeit

def main():
    # Measure time taken to execute extract_data
    start_time = timeit.default_timer()
    driver = wp.instantiate_driver()
    bookie_urls = config.url_creator(cts.BOOKIE_URLS)
    wp.extract_data(bookie_urls, driver)
    end_time = timeit.default_timer()
    
    print(f"Time taken: {end_time - start_time} seconds")
    driver.quit()

if __name__ == '__main__':
    main()