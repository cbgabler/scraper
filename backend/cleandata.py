from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

def load_database():
    mongo_uri = os.getenv("CONNECTION_STR")
    if not mongo_uri:
        print("Could not find string")
        return 0
    client = pymongo.MongoClient(mongo_uri)
    db = client["scrapedLines"]
    return db

def clean_data(db):
    query
    
