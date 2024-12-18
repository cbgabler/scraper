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
    database = client.get_database("scrapedLines")
    lines = database.get_collection("draftkings")

    query = { "date" : "today"}
    projection = {"moneyline" : 1, "team" : 1, "_id" : 0}
    cursor = lines.find(query, projection)

    for line in cursor:
        print(line)

    client.close()

def find_ev():
    database = client.get_database("scrapedLines")
    lines = database.get_collection("draftkings")

    query = { "date" : "today"}
    projection = {"moneyline" : 1, "team" : 1, "_id" : 0}
    cursor = lines.find(query, projection)

    for line in cursor:
        print(line)

    client.close()
def binary_search(arr):
    return 0

init_mongoose()