import os
import csv

# Path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'sport_csvs', 'dk_baseball_tomorrow.csv')

# Read the CSV file
def read_csv():
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)