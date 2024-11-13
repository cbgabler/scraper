import random
import csv
import os

team_names = [
    "STL Blues", "SEA Kraken", "BOS Bruins", "FLA Panthers", "CHI Blackhawks",
    "UTA Hockey Club", "TOR Maple Leafs", "NY Rangers", "MIA Heat", "LA Lakers",
    "DAL Mavericks", "ATL Hawks", "PHI 76ers", "SAC Kings", "DEN Nuggets",
    "LAL Lakers", "OKC Thunder", "GS Warriors", "BKN Nets", "IND Pacers",
    "DET Pistons", "MIL Bucks", "MIN Timberwolves", "ORL Magic", "MEM Grizzlies",
    "CHI Bulls", "HOU Rockets", "SAS Spurs", "CLE Cavaliers", "NY Knicks",
    "PHX Suns", "BOS Celtics", "GSW Warriors", "TOR Raptors", "PHI Eagles",
    "LA Clippers", "DAL Cowboys", "WAS Wizards", "MIA Dolphins", "BAL Ravens",
    "NY Jets", "CAR Panthers", "SEA Seahawks", "JAC Jaguars", "LV Raiders",
    "NE Patriots", "DET Lions", "KC Chiefs", "TEN Titans", "LA Rams"
]



def create_random_team_file(filename, num_lines):
    path = 'parser/tests/test_csvs/'
    with open(f"{path}{filename}", mode='w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Team", "Moneyline"])
        for _ in range(num_lines):
            team = random.choice(team_names)
            moneyline = random.choice([f"+{random.randint(100, 1500)}", f"−{random.randint(100, 1500)}"])
            writer.writerow([team, moneyline])

create_random_team_file("random_teams_1.csv", 50)
create_random_team_file("random_teams_2.csv", 50)
create_random_team_file("random_teams_3.csv", 50)
create_random_team_file("random_teams_4.csv", 50)
