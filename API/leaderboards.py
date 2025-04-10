import requests

"""
Get players on a specific leaderboard

Args:
    token (str): API token
    leaderboardId (str): ID of the leaderboard to fetch
    limit (int): Number of players to return
    after (str): Player tag to start after
    before (str): Player tag to end before

Returns:
[
  {
    "id": int,
    "name": str,
    "nameLocalized": {} // Likely an empty object for non-localized names
  },
  ... // More Leaderboard objects
]
"""
def leaderboard(token, leaderboardId, limit=None, after=None, before=None):
    url = f"https://api.clashroyale.com/v1/leaderboard/{leaderboardId}"
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
List leaderboards for different trophy roads

Args:
    token (str): API token

Returns:
[
  {
    "id": int,
    "name": str,
    "nameLocalized": {} // Likely an empty object for non-localized names
  },
  ... // More Leaderboard objects
]
"""
def leaderboards(token):
    url = f"https://api.clashroyale.com/v1/leaderboards"
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