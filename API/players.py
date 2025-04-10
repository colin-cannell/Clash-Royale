import requests

"""
Get information about a single player by player tag.

Args:
    token (str): The API token for authentication.
    playerTag (str): The player tag of the player to get information about.

Returns:
    dict: A dictionary containing player information if successful, None otherwise.
{
  "tag": str,
  "name": str,
  "expLevel": int,
  "trophies": int,
  "bestTrophies": int,
  "donations": int,
  "donationsReceived": int,
  "battleCount": int,
  "threeCrownWins": int,
  "challengeCardsWon": int,
  "challengeMaxWins": int,
  "tournamentCardsWon": int,
  "tournamentBattleCount": int,
  "warDayWins": int,
  "clanCardsCollected": int,
  "starPoints": int,
  "expPoints": int,
  "totalExpPoints": int,
  "legacyTrophyRoadHighScore": int,
  "role": str, // Enum: "member", "elder", "coLeader", "leader"
  "wins": int,
  "losses": int,
  "totalDonations": int,
  "clan": {
    "tag": str,
    "name": str,
    "badgeId": int,
    "badgeUrls": {
      "small": str,
      "medium": str,
      "large": str
    }
  },
  "arena": {
    "id": int,
    "name": str,
    "nameLocalized": {}, // Likely an empty object for non-localized names
    "iconUrls": {
      "medium": str
    }
  },
  "leagueStatistics": {
    "currentSeason": {
      "trophies": int,
      "bestTrophies": int,
      "rank": int,
      "id": str
    },
    "previousSeason": {
      "trophies": int,
      "bestTrophies": int,
      "rank": int,
      "id": str
    },
    "bestSeason": {
      "trophies": int,
      "bestTrophies": int,
      "rank": int,
      "id": str
    }
  },
  "currentDeck": [
    {
      "id": int,
      "nameLocalized": {}, // Likely an empty object for non-localized names
      "rarity": str, // Enum: "common", "rare", "epic", "legendary", "champion"
      "count": int,
      "level": int,
      "starLevel": int,
      "evolutionLevel": int,
      "maxLevel": int,
      "elixirCost": int,
      "maxEvolutionLevel": int,
      "iconUrls": {
        "medium": str
      },
      "used": bool
    },
    ...
  ],
  "currentDeckSupportCards": [
    {
      "id": int,
      "nameLocalized": {},
      "rarity": str,
      "count": int,
      "level": int,
      "starLevel": int,
      "evolutionLevel": int,
      "maxLevel": int,
      "elixirCost": int,
      "maxEvolutionLevel": int,
      "iconUrls": {
        "medium": str
      },
      "used": bool
    },
    ...
  ],
  "cards": [
    {
      "id": int,
      "nameLocalized": {},
      "rarity": str,
      "count": int,
      "level": int,
      "starLevel": int,
      "evolutionLevel": int,
      "maxLevel": int,
      "elixirCost": int,
      "maxEvolutionLevel": int,
      "iconUrls": {
        "medium": str
      },
      "used": bool
    },
    ...
  ],
  "supportCards": [
    {
      "id": int,
      "nameLocalized": {},
      "rarity": str,
      "count": int,
      "level": int,
      "starLevel": int,
      "evolutionLevel": int,
      "maxLevel": int,
      "elixirCost": int,
      "maxEvolutionLevel": int,
      "iconUrls": {
        "medium": str
      },
      "used": bool
    },
    ...
  ],
  "currentFavouriteCard": {
    // Structure of a PlayerItemLevel object (as above)
    "id": int,
    "nameLocalized": {},
    "rarity": str,
    "count": int,
    "level": int,
    "starLevel": int,
    "evolutionLevel": int,
    "maxLevel": int,
    "elixirCost": int,
    "maxEvolutionLevel": int,
    "iconUrls": {
      "medium": str
    },
    "used": bool
  },
  "badges": [
    {
      "name": str,
      "level": int,
      "maxLevel": int,
      "progress": int,
      "target": int,
      "iconUrls": {
        "medium": str
      }
    },
    ...
  ],
  "achievements": [
    {
      "nameLocalized": {},
      "infoLocalized": {},
      "completionInfoLocalized": {},
      "stars": int,
      "value": int,
      "target": int
    },
    ...
  ],
  "currentPathOfLegendSeasonResult": {
    "trophies": int,
    "rank": int,
    "leagueNumber": int
  },
  "lastPathOfLegendSeasonResult": {
    "trophies": int,
    "rank": int,
    "leagueNumber": int
  },
  "bestPathOfLegendSeasonResult": {
    "trophies": int,
    "rank": int,
    "leagueNumber": int
  },
  "progress": {} // Likely additional progress information, structure may vary
}
"""
def player(token, playerTag):
    url = f"https://api.clashroyale.com/v1/players/%23{playerTag.replace('#', '')}"  # Remove the '#' from the tag in case it is included.
    headers = {
        "Accept": "application/json",
        "authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching player data: {e}")
        return None
    except ValueError as e:  # Catch json decode errors.
        print(f"Error decoding json data: {e}")
        return None

"""
Get the battle logs of a player by player tag.

Args:
    token (str): The API token for authentication.
    playerTag (str): The player tag of the player to get battle logs for.

Returns:
[
  {
    "type": str, // Enum: "PvP", "clanWar", "challenge", "tournament", "casual", ... (more values possible)
    "battleTime": str (ISO 8601 format),
    "challengeId": int,
    "tournamentTag": str,
    "challengeTitle": str,
    "isLadderTournament": bool,
    "isHostedMatch": bool,
    "arena": {
      "id": int,
      "name": str,
      "nameLocalized": {}, // Likely an empty object for non-localized names
      "iconUrls": {
        "medium": str
      }
    },
    "gameMode": {
      "id": int,
      "name": str
    },
    "deckSelection": str, // Enum: "ladder", "challenge", "tournament", "friendly", ... (more values possible)
    "challengeWinCountBefore": int,
    "boatBattleSide": str,
    "boatBattleWon": bool,
    "newTowersDestroyed": int,
    "prevTowersDestroyed": int,
    "remainingTowers": int,
    "leagueNumber": int,
    "team": [
      {
        "tag": str,
        "name": str,
        "startingTrophies": int,
        "trophyChange": int,
        "kingTowerHitPoints": int,
        "princessTowersHitPoints": [
          int,
          int // Up to two princess towers
        ],
        "crowns": int,
        "clan": {
          "tag": str,
          "name": str,
          "badgeId": int,
          "badgeUrls": {
            "small": str,
            "medium": str,
            "large": str
          }
        },
        "cards": [
          {
            "id": int,
            "nameLocalized": {},
            "rarity": str, // Enum: "common", "rare", "epic", "legendary", "champion"
            "count": int,
            "level": int,
            "starLevel": int,
            "evolutionLevel": int,
            "maxLevel": int,
            "elixirCost": int,
            "maxEvolutionLevel": int,
            "iconUrls": {
              "medium": str
            },
            "used": bool
          },
          ...
        ],
        "supportCards": [
          {
            "id": int,
            "nameLocalized": {},
            "rarity": str,
            "count": int,
            "level": int,
            "starLevel": int,
            "evolutionLevel": int,
            "maxLevel": int,
            "elixirCost": int,
            "maxEvolutionLevel": int,
            "iconUrls": {
              "medium": str
            },
            "used": bool
          },
          ...
        ],
        "elixirLeaked": float,
        "globalRank": int,
        "rounds": [
          {
            "cards": [
              {
                "id": int,
                "nameLocalized": {},
                "rarity": str,
                "count": int,
                "level": int,
                "starLevel": int,
                "evolutionLevel": int,
                "maxLevel": int,
                "elixirCost": int,
                "maxEvolutionLevel": int,
                "iconUrls": {
                  "medium": str
                },
                "used": bool
              },
              ...
            ],
            "elixirLeaked": float,
            "crowns": int,
            "kingTowerHitPoints": int,
            "princessTowersHitPoints": [
              int,
              int // Up to two princess towers
            ]
          },
          ...
        ]
      },
      ... // More team members in 2v2
    ],
    "opponent": [
      {
        "tag": str,
        "name": str,
        "startingTrophies": int,
        "trophyChange": int,
        "kingTowerHitPoints": int,
        "princessTowersHitPoints": [
          int,
          int // Up to two princess towers
        ],
        "crowns": int,
        "clan": {
          "tag": str,
          "name": str,
          "badgeId": int,
          "badgeUrls": {
            "small": str,
            "medium": str,
            "large": str
          }
        },
        "cards": [
          {
            "id": int,
            "nameLocalized": {},
            "rarity": str, // Enum: "common", "rare", "epic", "legendary", "champion"
            "count": int,
            "level": int,
            "starLevel": int,
            "evolutionLevel": int,
            "maxLevel": int,
            "elixirCost": int,
            "maxEvolutionLevel": int,
            "iconUrls": {
              "medium": str
            },
            "used": bool
          },
          ...
        ],
        "supportCards": [
          {
            "id": int,
            "nameLocalized": {},
            "rarity": str,
            "count": int,
            "level": int,
            "starLevel": int,
            "evolutionLevel": int,
            "maxLevel": int,
            "elixirCost": int,
            "maxEvolutionLevel": int,
            "iconUrls": {
              "medium": str
            },
            "used": bool
          },
          ...
        ],
        "elixirLeaked": float,
        "globalRank": int,
        "rounds": [
          {
            "cards": [
              {
                "id": int,
                "nameLocalized": {},
                "rarity": str,
                "count": int,
                "level": int,
                "starLevel": int,
                "evolutionLevel": int,
                "maxLevel": int,
                "elixirCost": int,
                "maxEvolutionLevel": int,
                "iconUrls": {
                  "medium": str
                },
                "used": bool
              },
              ...
            ],
            "elixirLeaked": float,
            "crowns": int,
            "kingTowerHitPoints": int,
            "princessTowersHitPoints": [
              int,
              int // Up to two princess towers
            ]
          },
          ...
        ]
      },
      ... // More opponents in 2v2
    ]
  },
  ... // More Battle objects
]
"""
def battle_logs(token, playerTag):
    url = f"https://api.clashroyale.com/v1/players/%23{playerTag.replace('#', '')}/battlelog"  # Remove the '#' from the tag in case it is included.
    headers = {
        "Accept": "application/json",
        "authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching player data: {e}")
        return None
    except ValueError as e:  # Catch json decode errors.
        print(f"Error decoding json data: {e}")
        return None