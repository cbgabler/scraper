class SofaScoreConstants:
    DEFAULT_URL = "https://www.sofascore.com/player/"
    PLAYER_NUM = 885203

class DraftKingsConstants:
    DEFAULT_URL = "https://sportsbook.draftkings.com/?category=game-lines&subcategory="
    MAIN_DIV = "parlay-card-10-a"
    TEAM_TYPE = "div"
    TEAM_HTML = "event-cell__name-text"
    ML_TYPE = "span"
    ML_HTML = "sportsbook-odds american no-margin default-color"

class FanDuelConstants:
    ## TODO doesnt work lol, need to figure out rotating class types
    DEFAULT_URL = "https://sportsbook.fanduel.com/navigation/"
    MAIN_DIV = "t h"
    TEAM_TYPE = "span"
    TEAM_HTML = "s t jc jd je jf gl gm gn ie jg h em bo jh bf"
    ML_TYPE = "span"
    ML_HTML = "jk jl em eg js jt bc"

class B365Constants:
    DEFAULT_URL = "https://www.co.bet365.com/?_h=igY5S8b4-5qJlZ0HlXWE4A%3D%3D#/AC/"
    MAIN_DIV = "gl-MarketGroup_Wrapper src-MarketGroup_Container "
    TEAM_TYPE = "div"
    TEAM_HTML = {"baseball" : "sbb-ParticipantTwoWayWithPitchersBaseball_Team ",
                 "basketball" : "scb-ParticipantFixtureDetailsHigherBasketball_Team ",
                 "hockey" : "sci-ParticipantFixtureDetailsHigherIceHockey_Team "}
    ML_TYPE = "div"
    ML_HTML = {"baseball" : "sac-ParticipantCenteredStacked60OTB_Odds",
               "basketball" : "sac-ParticipantOddsOnly50OTB_Odds",
               "hockey" : "sac-ParticipantOddsOnly50OTB_Odds"}

LEAGUES = {"baseball" :"mlb",
           "basketball" :"nba",
           "hockey" : "nhl",
           }

B365 = {"baseball" : "B16/C20525425/D48/E1096/F10/",
        "basketball" : "B18/C20604387/D48/E1453/F10/",
        "hockey" : "B17/C20836572/D48/E972/F10/",
        "football" : "B12/C20426855/D48/E1441/F36/"}

SPORTS = {"baseball",
          "basketball",
          "hockey",
          "football"
          }
