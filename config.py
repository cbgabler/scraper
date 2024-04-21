def sofa_url_creator(input_url, id_num):
    first_name, last_name = input("Please enter the player name you wish to pull (first and last): ").split()
    sofa_url = f"{input_url}/{first_name}-{last_name}/{id_num}"
    return sofa_url

def url_creator(bookie_urls, sports):
    final_urls = {}
    for bookie, url in bookie_urls.items():
        final_urls[bookie] = {}
        for sport in sports:
            final_urls[bookie][sport] = f"{url}{sport}"
    print(final_urls)
    return final_urls