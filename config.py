sport = input("Which sport would you like to search for?: ")

def sofa_url_creator(input_url, id_num):
    first_name, last_name = input("Please enter the player name you wish to pull (first and last): ").split()
    sofa_url = f"{input_url}/{first_name}-{last_name}/{id_num}"
    return sofa_url

def url_creator(bookie_urls):
    final_urls = {}
    for bookie, url in bookie_urls.items():
        if bookie == "dk":
            dk_url = f"{url}{sport}"
            final_urls[bookie] = dk_url
        elif bookie == "bv":
            bv_url = f"{url}{sport}/mlb" # change this to another constant later
            final_urls[bookie] = bv_url
        print(final_urls)
    return final_urls