import unittest
import web_parse
import config
import constants as cts
import compare_lines as cl

class TestParse(unittest.TestCase):
    def test_config(self):
        self.assertEqual(config.dk_url_creator(cts.DraftKingsConstants.DEFAULT_URL, "baseball"), "https://sportsbook.draftkings.com/leagues/baseball")
    

    def test_compare(self):
        print(cl.find_most_profitable_bet("./sport_csvs/MGMGrand_football_halftime.csv"))
        self.assertEqual(cl.find_most_profitable_bet("../sport_csvs/MGMGrand_football_halftime.csv"))

class TestComapre(unittest.TestCase):
    def test_compare(self):
        print

if __name__ == '__main__':
    unittest.main()