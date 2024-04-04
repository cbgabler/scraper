def sofa_url_creator(input_url, id_num):
    first_name, last_name = input("Please enter the player name you wish to pull (first and last): ").split()
    sofa_url = f"{input_url}/{first_name}-{last_name}/{id_num}"
    return sofa_url

def draftkings_url_creator(input_url):
    sport = input("Which sport would you like to search for?: ")
    dk_url = f"{input_url}{sport}"
    return dk_url