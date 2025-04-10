import requests

"""
Get list of available cards

Args:
    token (str): API token
    limit (int): Number of cards to return
    after (str): Card ID to start after
    before (str): Card ID to end before

Returns:
{
  "items": [
    {
      "id": int,
      "name": str,
      "nameLocalized": {}, // Likely an empty object for non-localized names
      "rarity": str, // Enum: "common", "rare", "epic", "legendary", "champion"
      "maxLevel": int,
      "elixirCost": int,
      "maxEvolutionLevel": int,
      "iconUrls": {
        "medium": str
      }
    },
    ...
  ],
  "supportItems": [
    {
      "id": int,
      "name": str,
      "nameLocalized": {},
      "rarity": str,
      "maxLevel": int,
      "elixirCost": int,
      "maxEvolutionLevel": int,
      "iconUrls": {
        "medium": str
      }
    },
    ...
  ]
}
"""
def cards(token, limit=None, after=None, before=None):
    url = f"https://api.clashroyale.com/v1/cards"
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
