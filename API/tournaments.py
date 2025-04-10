import requests

"""
Search all tournaments by name

Args:
    token (str): API token
    name (str): Name of the tournament to search for
    limit (int): Number of tournaments to return
    after (str): Tournament ID to start after
    before (str): Tournament ID to end before

Result:
[
  {
    "tag": str,
    "name": str,
    "description": str,
    "status": str, // Enum: "open", "full", "ended", "preparation"
    "type": str, // Enum: "open", "passwordProtected", "private"
    "creatorTag": str,
    "capacity": int,
    "maxCapacity": int,
    "levelCap": int,
    "preparationDuration": int,
    "duration": int,
    "createdTime": str (ISO 8601 format),
    "firstPlaceCardPrize": int,
    "gameMode": {
      "id": int,
      "name": str
    }
  },
  ... // More TournamentHeader objects
]
"""
def tournaments(token, name=None, limit=None, after=None, before=None):
    url = f"https://api.clashroyale.com/v1/tornaments"
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
Get information about a single tournament by a tournament tag.

Ags: 
    token (str): API token
    tournamentTag (str): Tournament tag to search for

Result:
{
  "tag": str,
  "name": str,
  "description": str,
  "status": str, // Enum: "open", "full", "ended", "preparation"
  "type": str, // Enum: "open", "passwordProtected", "private"
  "creatorTag": str,
  "capacity": int,
  "maxCapacity": int,
  "levelCap": int,
  "preparationDuration": int,
  "duration": int,
  "createdTime": str (ISO 8601 format),
  "startedTime": str (ISO 8601 format, may be null if not started),
  "endedTime": str (ISO 8601 format, may be null if not ended),
  "firstPlaceCardPrize": int,
  "gameMode": {
    "id": int,
    "name": str
  },
  "membersList": [
    {
      "tag": str,
      "name": str,
      "rank": int,
      "previousRank": int,
      "score": int,
      "clan": {
        "tag": str,
        "name": str,
        "badgeId": int,
        "badgeUrls": {
          "small": str,
          "medium": str,
          "large": str
        }
      }
    },
    ...
  ]
}
"""
def tournament(token, tournamentTag):
    url = f"https://api.clashroyale.com/v1/tournaments/%23{tournamentTag.replace('#', '')}"
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

