class SofaScoreConstants:
    DEFAULT_URL = "https://www.sofascore.com/player/"
    PLAYER_NUM = 885203

class DraftKingsConstants:
    DEFAULT_URL = "https://sportsbook.draftkings.com/leagues/"
    MAIN_DIV = "parlay-card-10-a"
    TEAM_TYPE = "div"
    TEAM_HTML = "event-cell__name-text"
    ML_TYPE = "span"
    ML_HTML = "sportsbook-odds american no-margin default-color"

class FanDuelConstants:
    ## TODO doesnt work, need to figure out rotating class types
    DEFAULT_URL = "https://sportsbook.fanduel.com/navigation/"
    MAIN_DIV = "t h"
    TEAM_TYPE = "span"
    TEAM_HTML = "s t jc jd je jf gl gm gn ie jg h em bo jh bf"
    ML_TYPE = "span"
    ML_HTML = "jk jl em eg js jt bc"

class B365Constants:
    DEFAULT_URL = "https://www.az.bet365.com/?_h=kwy6Qk35g2O4lxEqWVcUVg%3D%3D&btsffd=1#/"
    MAIN_DIV = "gl-MarketGroup_Wrapper src-MarketGroup_Container "
    TEAM_TYPE = "div"
    TEAM_HTML = {"baseball" : "sbb-ParticipantTwoWayWithPitchersBaseball_Team ",
                 "basketball" : "scb-ParticipantFixtureDetailsHigherBasketball_Team ",
                 "hockey" : "sci-ParticipantFixtureDetailsHigherIceHockey_Team ",
                 "football" : "sac-ParticipantFixtureDetailsHigherAmericanFootball_Team"}
    ML_TYPE = "span"
    ML_HTML = {"baseball" : "sac-ParticipantCenteredStacked60OTB_Odds",
               "basketball" : "sac-ParticipantOddsOnly50OTB_Odds",
               "hockey" : "sac-ParticipantOddsOnly50OTB_Odds",
               "football" : "sac-ParticipantOddsOnly50OTB_Odds"}
    
class BetUSConstants:
    DEFAULT_URL = "https://www.betus.com.pa/sportsbook/"
    MAIN_DIV = "game-block "
    TEAM_TYPE = "span"
    TEAM_HTML = "awayName"
    ML_TYPE = "a"
    ML_HTML = "ctl00_ctl00_M_middle_MarketConstructor1_ConstructorLines1_GameLines1_repHeaders_ctl00_repLines_ctl00_lblBetVisitorMoneyLine"

class MGMConstants:
    DEFAULT_URL = "https://sports.az.betmgm.com/en/sports/"
    MAIN_DIV = "main-view"
    TEAM_TYPE = "div"
    TEAM_HTML = "participant"
    ML_TYPE = "span"
    ML_HTML = "custom-odds-value-style ng-star-inserted"

LEAGUES = {"baseball" :"mlb",
           "basketball" :"nba",
           "hockey" : "nhl"
           }

B365 = {"baseball" : "B16/C20525425/D48/E1096/F10/",
        "basketball" : "B18/C20604387/D48/E1453/F10/",
        "hockey" : "B17/C20836572/D48/E972/F10/",
        "football" : "AC/B12/C20426855/D48/E1441/F36/"}

SPORTS = {"baseball",
          "basketball",
          "hockey",
          "football"
          }
