def sofa_url_creator(input_url, id_num):
    first_name, last_name = input("Please enter the player name you wish to pull (first and last): ").split()
    sofa_url = f"{input_url}/{first_name}-{last_name}/{id_num}"
    return sofa_url

def dk_url_creator(dk_url, sports):
    dk_urls = {}
    for sport in sports:
        dk_urls[sport] = f"{dk_url}{sport}"
    print(dk_urls)
    return dk_urls