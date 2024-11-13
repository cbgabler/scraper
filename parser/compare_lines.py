from flask import Flask, render_template
import os
import csv

app = Flask(__name__)

# Path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'sport_csvs', 'dk_baseball_tomorrow.csv')

# Read the CSV file
def read_csv():
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data

@app.route('/')
def index():
    data = read_csv()
    return render_template('index.html', data=data)

import csv

def find_most_profitable_bet(file_paths):
    most_profitable_bet = None

    for file_path in file_paths:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                team = row['Team']
                odds = row['Moneyline']
                print(team, odds)
    
    return most_profitable_bet

find_most_profitable_bet('parser/tests/test_csvs/random_teams_1.csv')

