import unittest
import web_parse
import config
import constants as cts

class TestParse(unittest.TestCase):
    def test_config(self):
        self.assertEqual(config.dk_url_creator(cts.DraftKingsConstants.DEFAULT_URL, "baseball"), "https://sportsbook.draftkings.com/leagues/baseball")
    



if __name__ == '__main__':
    unittest.main()