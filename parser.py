from bs4 import BeautifulSoup
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'
}

first_name, last_name = input("Which player would you like to see statistics for? (first name, last name): ").split()
player_number = str(885203)

url = f"https://www.sofascore.com/player/{first_name.lower()}-{last_name.lower().replace(' ', '-')}/{player_number}#tab:matches"

try:
    page_scraping = requests.get(url, headers=headers)
    page_scraping.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

soup = BeautifulSoup(page_scraping.text, "html.parser")

# Update the class name to match the actual class in the HTML
points = soup.findAll("span", attrs={"class": "sc-d392def8-0 hkPGsE"})

with open("scraped_quotes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([f"POINTS FOR {first_name} {last_name}"])
    if not points:
        print("No points found")
    for point_count in points:
        print("Hit")
        print(point_count.text)

