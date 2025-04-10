import requests

"""
Get current and upcoming challenges. 

Args:
    token (str): API token

Returns:
{
  "items": [
    {
      "title": str,
      "titleLocalized": {}, // Likely an empty object for non-localized titles
      "type": str, // Enum: "normal", "grand"
      "startTime": str (ISO 8601 format),
      "endTime": str (ISO 8601 format),
      "challenges": [
        {
          "id": int,
          "name": str,
          "nameLocalized": {}, // Likely an empty object for non-localized names
          "description": str,
          "descriptionLocalized": {}, // Likely an empty object for non-localized descriptions
          "winMode": str,
          "casual": bool,
          "maxLosses": int,
          "maxWins": int,
          "iconUrl": str,
          "gameMode": {
            "id": int,
            "name": str
          },
          "prizes": [
            {
              "type": str, // Enum: "card", "resource", "chest", "consumable", "currency", "token", "star_points"
              "rarity": str, // Enum: "common", "rare", "epic", "legendary", "champion"
              "chest": str,
              "resource": str, // Enum: "gold", "gems"
              "amount": int,
              "cardItem": { // Structure of a PlayerItemLevel object (see Player object)
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
              "consumableName": str,
              "wins": int
            },
            ...
          ]
        },
        ...
      ]
    },
    ...
  ]
}
"""
def challenges(token):
    url = f"https://api.clashroyale.com/v1/challenges"
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