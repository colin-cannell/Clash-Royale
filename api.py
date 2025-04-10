import requests

from API.clans import *
from API.players import *
from API.cards import *
from API.tournaments import *
from API.challenges import *
from API.leaderboards import *

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ2YWM4ZTI1LTI1NDgtNDAzMC1iN2MyLWNmZmI1NGI4ODVjOSIsImlhdCI6MTc0NDE1MzUxNywic3ViIjoiZGV2ZWxvcGVyLzM5NWYyZDdhLTlkZWUtZGJlNC1iYzdhLTVlNmMzOTdiYWJmZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3NC4yMTMuMjM2LjY1Il0sInR5cGUiOiJjbGllbnQifV19.4e7rJ2hGNz1fOhXpdDKPQYHhsKMyaYHJpJAQMwwMTsAJtKKWBwl4v4Pi76TwgymhXjV7pfKKIioQykeRiJ5tbA"

cheifburger = "#820GP2VQ"
echo = '#C00Y2PJ9'

logs = battle_logs(token, echo)
for log in reversed(logs):
    if log['gameMode']["name"] == 'Draft_Competitive':
        for card in log["team"][0]["cards"]:
            print(card["name"])
        print("---------------------")

    
    