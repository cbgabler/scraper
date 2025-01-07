from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("CONNECTION_STR")

client = MongoClient(uri)

try:
    database = client.get_database("scrapedLines")
    movies = database.get_collection("draftkings")

    query = { "date": "today" }
    movie = movies.find_one(query)

    print(movie)

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)

def init_mongoose():
    ## choice = input("What would you like to search for? ")
    choice = "BOS Celtics"

    database = client.get_database("scrapedLines")
    lines = database.get_collection("draftkings")

    query = { "team" : f"{choice}"}
    projection = {"moneyline" : 1, "_id" : 0}
    cursor = lines.find(query, projection)

    return cursor

def compare_lines(data):
    norm = []
    for line in data:
        norm.append(normalize_data(line.get("moneyline")))
    print(norm)
    ## testing = float(input("What would you like to bet? "))
    margins = []
    for i in norm: ## speed up later // bin search.
        for j in norm:
            margin = 1 - 1/(1/i+1/j)
            margins.append(margin)
    print(1-1/(1/1.45 + 1/2.84))
    print(margins)
    for i in margins:
        if i > 0:
            print("ARB!" + f"{i * 100}%")

def normalize_data(val):
    normalized = []
    normalized_line = val
    if normalized_line[0] == '+':
        normalized_line = int(normalized_line[1::]) / 100 + 1
    else:
        normalized_line = 100 / int(normalized_line[1::]) + 1

    return float(normalized_line)

def multiply_profit(norm, testing):
    func = lambda x, money: x * money
    for i in range(len(norm)):
        norm[i] = func(norm[i], testing)

compare_lines(init_mongoose())
client.close()