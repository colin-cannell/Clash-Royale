import requests

"""
Retrieve the clan war log for a specific clan.

Args:
    token (str): The API token for authentication.
    clanTag (str): The tag of the clan (e.g., '#ABC123XYZ').
    limit (int, optional): Limit the number of war log entries returned. Defaults to None (API default).
    after (str, optional): Return only war log entries that occurred after this cursor. Defaults to None.
    before (str, optional): Return only war log entries that occurred before this cursor. Defaults to None.

Returns:
    dict: A dictionary containing the clan war log data. The structure is as follows:
        {
          "items": [
            {
              "seasonId": int,
              "createdTime": str (ISO 8601 format),
              "participants": [
                {
                  "tag": str,
                  "name": str,
                  "cardsEarned": int,
                  "battlesPlayed": int,
                  "wins": int,
                  "collectionDayBattlesPlayed": int,
                  "numberOfBattles": int (may vary or be absent)
                },
                ...
              ],
              "standings": [
                {
                  "clan": {
                    "tag": str,
                    "name": str,
                    "...": "other clan details" (if available)
                  },
                  "trophyChange": int,
                  "...": "other standing details" (if available)
                },
                ...
              ]
            },
            ...
          ],
          "paging": {
            "cursors": {
              "after": str (cursor for next page, if applicable),
              "before": str (cursor for previous page, if applicable)
            }
          }
        }
"""
def war_log(token, clanTag, limit=None, after=None, before=None):
    url = f"https://api.clashroyale.com/v1/clans/{clanTag}/warlog"
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
    except ValueError as e: # Catch json decode errors.
        print(f"Error decoding json data: {e}")
        return None    
    
"""
Search all clans by name and/or filtering the results using various criteria.

Args:
    token (str): The API token for authentication.
    name (str): The name of the clan to search for.
    locationId (int, optional): The ID of the location to filter clans by. Defaults to None.
    minMembers (int, optional): Minimum number of members in the clan. Defaults to None.
    maxMembers (int, optional): Maximum number of members in the clan. Defaults to None.
    minScore (int, optional): Minimum score of the clan. Defaults to None.
    limit (int, optional): Limit the number of clans returned. Defaults to None.
    after (str, optional): Return only clans that occurred after this cursor. Defaults to None.
    before (str, optional): Return only clans that occurred before this cursor. Defaults to None.

Returns:
    dict: A dictionary containing the search results. The structure is as follows:
       {
        "items": [
            {
            "tag": str,
            "name": str,
            "type": str,  // Enum: "open", "inviteOnly", "closed"
            "description": str,
            "badgeId": int,
            "clanScore": int,
            "clanWarTrophies": int,
            "requiredTrophies": int,
            "members": int,
            "clanChestStatus": str, // Enum: "inactive", "active", "full", "unavailable"
            "clanChestLevel": int,
            "clanChestMaxLevel": int,
            "donationsPerWeek": int,
            "badgeUrls": {
                "small": str,
                "medium": str,
                "large": str
            },
            "location": {
                "id": int,
                "name": str,
                "isCountry": bool,
                "countryCode": str // Only present if isCountry is true
            },
            "memberList": [
                {
                "tag": str,
                "name": str,
                "role": str, // Enum: "member", "elder", "coLeader", "leader"
                "expLevel": int,
                "trophies": int,
                "clanRank": int,
                "previousClanRank": int,
                "donations": int,
                "donationsReceived": int,
                "lastSeen": str (ISO 8601 format),
                "clanChestPoints": int,
                "arena": {
                    "id": int,
                    "name": str,
                    "iconUrls": {
                    "medium": str
                    },
                    "nameLocalized": {} // Likely an empty object for non-localized names
                }
                },
                ...
            ],
            "clanChestPoints": int // Duplicate of the top-level clanChestPoints? May be redundant.
            },
            ...
        ],
        "paging": {
            "cursors": {
            "after": str,
            "before": str
            }
        }
    }
"""
def clans(token, name=None, locationId=None, minMembers=None, maxMembers=None, minScore=None, limit=None, after=None, before=None):
    url = f"https://api.clashroyale.com/v1/clans"
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
    except ValueError as e: # Catch json decode errors.
        print(f"Error decoding json data: {e}")

"""
Retreive clans river race log

Args:
    token (str): The API token for authentication.
    clanTag (str): The tag of the clan (e.g., '#ABC123XYZ').
    limit (int, optional): Limit the number of war log entries returned. Defaults to None (API default).
    after (str, optional): Return only war log entries that occurred after this cursor. Defaults to None.
    before (str, optional): Return only war log entries that occurred before this cursor. Defaults to None.

Returns:
    {
    "items": [
        {
        "seasonId": int,
        "createdTime": str (ISO 8601 format),
        "sectionIndex": int,
        "standings": [
            {
            "rank": int,
            "trophyChange": int,
            "clan": {
                "tag": str,
                "name": str,
                "badgeId": int,
                "clanScore": int,
                "fame": int,
                "repairPoints": int,
                "finishTime": str (ISO 8601 format, may be null if not finished),
                "periodPoints": int,
                "participants": [
                {
                    "tag": str,
                    "name": str,
                    "fame": int,
                    "repairPoints": int,
                    "boatAttacks": int,
                    "decksUsed": int,
                    "decksUsedToday": int
                },
                ...
                ]
            }
            },
            ...
        ]
        },
        ...
    ],
    "paging": {
        "cursors": {
        "after": str,
        "before": str
        }
    }
}
"""
def river_race_log(token, clanTag, limit=None, after=None, before=None):
    url = f"https://api.clashroyale.com/v1/clans/{clanTag}/riverracelog"
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
    except ValueError as e: # Catch json decode errors.
        print(f"Error decoding json data: {e}")

"""
Retrieve information about clan's current clan war

Args:
    token (str): The API token for authentication.
    clanTag (str): The tag of the clan (e.g., '#ABC123XYZ').

Returns:
        {
  "state": str,  // Enum: "clanNotFound", "accessDenied", "notInWar", "collectionDay", "matchmaking", "warDay", "ended"
  "clan": {
    "tag": str,
    "name": str,
    "badgeId": int,
    "clanScore": int,
    "participants": int,
    "battlesPlayed": int,
    "wins": int,
    "crowns": int
  },
  "participants": [
    {
      "tag": str,
      "name": str,
      "cardsEarned": int,
      "battlesPlayed": int,
      "wins": int,
      "collectionDayBattlesPlayed": int,
      "numberOfBattles": int // Note: This might not always be present or have a consistent meaning across all war types.
    },
    ...
  ],
  "clans": [
    {
      "tag": str,
      "name": str,
      "badgeId": int,
      "clanScore": int,
      "participants": int,
      "battlesPlayed": int,
      "wins": int,
      "crowns": int
    },
    ...
  ],
  "collectionEndTime": str (ISO 8601 format),
  "warEndTime": str (ISO 8601 format)
}

"""
def current_war(token, clanTag):
    url = f"https://api.clashroyale.com/v1/clans/%23{clanTag}/currentwar"
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
    except ValueError as e: # Catch json decode errors.
        print(f"Error decoding json data: {e}")
    
"""
Get information about a single clan by clan tag.
Args:
    token (str): The API token for authentication.
    clanTag (str): The tag of the clan (e.g., '#ABC123XYZ').

Returns:
    {
  "tag": str,
  "name": str,
  "type": str,  // Enum: "open", "inviteOnly", "closed"
  "description": str,
  "badgeId": int,
  "clanScore": int,
  "clanWarTrophies": int,
  "requiredTrophies": int,
  "members": int,
  "clanChestStatus": str, // Enum: "inactive", "active", "completed", "unknown"
  "clanChestLevel": int,
  "clanChestMaxLevel": int,
  "donationsPerWeek": int,
  "badgeUrls": {
    "small": str,
    "medium": str,
    "large": str
  },
  "location": {
    "id": int,
    "name": str,
    "localizedName": str,
    "isCountry": bool,
    "countryCode": str // Only present if isCountry is true
  },
  "memberList": [
    {
      "tag": str,
      "name": str,
      "role": str, // Enum: "member", "elder", "coLeader", "leader"
      "expLevel": int,
      "trophies": int,
      "clanRank": int,
      "previousClanRank": int,
      "donations": int,
      "donationsReceived": int,
      "lastSeen": str (ISO 8601 format),
      "clanChestPoints": int,
      "arena": {
        "id": int,
        "name": str,
        "nameLocalized": {}, // Likely an empty object for non-localized names
        "iconUrls": {
          "medium": str
        }
      }
    },
    ...
  ],
  "clanChestPoints": int // Duplicate of the top-level clanChestPoints? May be redundant.
}
"""
def clan(token, clanTag):
    url = f"https://api.clashroyale.com/v1/clans/{clanTag}"
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
    except ValueError as e: # Catch json decode errors.
        print(f"Error decoding json data: {e}")

"""
List clan members.

Args:
    token (str): The API token for authentication.
    clanTag (str): The tag of the clan (e.g., '#ABC123XYZ').
    limit (int, optional): Limit the number of members returned. Defaults to None.
    after (str, optional): Return only members that occurred after this cursor. Defaults to None.
    before (str, optional): Return only members that occurred before this cursor. Defaults to None. 

Returns:
[
  {
    "tag": str,
    "name": str,
    "role": str,  // Enum: "notMember", "member", "leader", "admin", "coLeader"
    "expLevel": int,
    "trophies": int,
    "clanRank": int,
    "previousClanRank": int,
    "donations": int,
    "donationsReceived": int,
    "lastSeen": str (ISO 8601 format),
    "clanChestPoints": int,
    "arena": {
      "id": int,
      "name": str,
      "nameLocalized": {}, // Likely an empty object for non-localized names
      "iconUrls": {
        "medium": str
      }
    }
  },
  ... // More ClanMember objects
]

"""
def members(token, clanTag, limit, after, before):
    url = f"https://api.clashroyale.com/v1/clans/{clanTag}/members"
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
    except ValueError as e: # Catch json decode errors.
        print(f"Error decoding json data: {e}")

"""
Retrieve information about clan's current river race

Args:
    token (str): The API token for authentication.
    clanTag (str): The tag of the clan (e.g., '#ABC123XYZ').

Returns:
    {
  "state": str, // Enum: "clanNotFound", "accessDenied", "matchmaking", "matched", "full", "ended"
  "clan": {
    "tag": str,
    "name": str,
    "badgeId": int,
    "clanScore": int,
    "fame": int,
    "repairPoints": int,
    "finishTime": str (ISO 8601 format, may be null),
    "periodPoints": int,
    "participants": [
      {
        "tag": str,
        "name": str,
        "fame": int,
        "repairPoints": int,
        "boatAttacks": int,
        "decksUsed": int,
        "decksUsedToday": int
      },
      ...
    ]
  },
  "clans": [
    {
      "tag": str,
      "name": str,
      "badgeId": int,
      "clanScore": int,
      "fame": int,
      "repairPoints": int,
      "finishTime": str (ISO 8601 format, may be null),
      "periodPoints": int,
      "participants": [
        {
          "tag": str,
          "name": str,
          "fame": int,
          "repairPoints": int,
          "boatAttacks": int,
          "decksUsed": int,
          "decksUsedToday": int
        },
        ...
      ]
    },
    ...
  ],
  "collectionEndTime": str (ISO 8601 format),
  "warEndTime": str (ISO 8601 format),
  "sectionIndex": int,
  "periodIndex": int,
  "periodType": str, // Enum: "training", "warDay", "colosseum"
  "periodLogs": [
    {
      "periodIndex": int,
      "items": [
        {
          "clan": {
            "tag": str
          },
          "pointsEarned": int,
          "progressStartOfDay": int,
          "progressEndOfDay": int,
          "endOfDayRank": int,
          "progressEarned": int,
          "numOfDefensesRemaining": int,
          "progressEarnedFromDefenses": int
        },
        ...
      ]
    },
    ...
  ]
}
"""
def current_river_race(token, clanTag):
    url = f"https://api.clashroyale.com/v1/clans/{clanTag}/currentriverrace"
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
    except ValueError as e: # Catch json decode errors.
        print(f"Error decoding json data: {e}")


