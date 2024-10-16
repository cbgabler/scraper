def sofa_url_creator(input_url, id_num):
    first_name, last_name = input("Please enter the player name you wish to pull (first and last): ").split()
    sofa_url = f"{input_url}/{first_name}-{last_name}/{id_num}"
    return sofa_url

def dk_url_creator(dk_url, leagues):
    dk_urls = {}
    for sport, league in leagues.items():
        dk_urls[sport] = f"{dk_url}{sport}/{league}"
    return dk_urls

def b365_url_creator(fd_url, ends):
    b365_urls = {}
    for sport, end in ends.items():
        b365_urls[sport] = f"{fd_url}{end}"
    return b365_urls

def betus_url_creator(betus_url, leagues):
    betus_urls ={}
    for sport, league in leagues.items():
        betus_urls[sport] = f"{betus_url}{league}"
    return betus_urls

def mgm_url_creator(mgm_url, sports):
    mgm_urls = {}
    for sport in sports:
        mgm_urls[sport] = f"{mgm_url}{sport}"
    return mgm_urls