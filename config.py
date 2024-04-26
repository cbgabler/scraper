def sofa_url_creator(input_url, id_num):
    first_name, last_name = input("Please enter the player name you wish to pull (first and last): ").split()
    sofa_url = f"{input_url}/{first_name}-{last_name}/{id_num}"
    return sofa_url

def dk_url_creator(dk_url, sports):
    dk_urls = {}
    for sport in sports:
        dk_urls[sport] = f"{dk_url}{sport}"
    return dk_urls

def b365_url_creator(fd_url, ends):
    b365_urls = {}
    for sport, end in ends.items():
        print(sport, end)
        b365_urls[sport] = f"{fd_url}{end}"
    return b365_urls