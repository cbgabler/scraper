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

# Endpoint to display the CSV data in your HTML
@app.route('/')
def index():
    data = read_csv()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
