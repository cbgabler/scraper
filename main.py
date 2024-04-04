import web_parse as wp
import config
import constants as cts
import timeit

def main():
    # Measure time taken to execute extract_points
    start_time = timeit.default_timer()
    driver = wp.instantiate_driver()
    player_url = config.draftkings_url_creator(cts.DK_DEFAULT_URL)
    source = wp.start_driver(player_url, driver)
    wp.extract_dk(source)
    end_time = timeit.default_timer()
    
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()