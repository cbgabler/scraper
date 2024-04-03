def url_creator(input_url, id_num):
    first_name, last_name = input("Please enter the player name you wish to pull (first and last): ").split()
    print(first_name, last_name)
    new_url = f"{input_url}/{first_name}-{last_name}/{id_num}"
    return new_url

