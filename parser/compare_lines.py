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

def find_highest_ev(file_paths)
    for file in file_paths:

def find_most_profitable_bet(file_path):
    most_profitable_bet = None
    max_profit = -float('inf')

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            bet = row['Bet']
            odds = float(row['Odds'])
            stake = float(row['Stake'])
            profit = (odds * stake) - stake
            if profit > max_profit:
                max_profit = profit
                most_profitable_bet = {
                    'Bet': bet,
                    'Odds': odds,
                    'Stake': stake,
                    'Profit': profit
                }
    
    return most_profitable_bet


file_path = 'betting_data.csv'
most_profitable_bet = find_most_profitable_bet(file_path)

if most_profitable_bet:
    print(f"The most profitable bet is: {most_profitable_bet['Bet']}")
    print(f"Odds: {most_profitable_bet['Odds']}")
    print(f"Stake: {most_profitable_bet['Stake']}")
    print(f"Profit: {most_profitable_bet['Profit']:.2f}")
else:
    print("No bets found.")


if __name__ == '__main__':
    app.run(debug=True)
