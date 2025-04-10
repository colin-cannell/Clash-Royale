import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

tripple_draft_cards_url = "https://royaleapi.com/game-mode/triple-draft?lang=en"
tripple_draft_best_cards_url = "https://royaleapi.com/cards/popular?time=7d&mode=grid&cat=TripleDraft&sort=rating"
data = "data/trippledraft/card_data.csv"
stats = "https://statsroyale.com/card/"

def extract_card_data_royale_api(url):
    """
    Scrapes card names and their statistics from the RoyaleAPI popular cards page.

    Args:
        url (str): The URL of the RoyaleAPI popular cards page.

    Returns:
        list: A list of dictionaries, where each dictionary contains
              the card name and its rating and usage.
              Returns an empty list if there's an issue fetching or parsing the data.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = bs(response.content, 'html.parser')
        card_data = {}

        # Find all the individual card containers
        cards = soup.find_all('div', class_='grid_item')
        for card in cards:
            data = card.attrs
            name = data.get('data-card')
            rating = data.get('data-rating')
            usage = data.get('data-usage')
            usage_delta = data.get('data-delta')
            win_precent = data.get('data-winpercent')
            win_delta = data.get('data-windelta')
            cwr = data.get('data-cleanwinrate')

            if name:
                card_data[name] = {
                    'rating': rating,
                    'usage': usage,
                    'usage_delta': usage_delta,
                    'win_precent': win_precent,
                    'win_delta': win_delta,
                    'cwr': cwr
                }
        return card_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    except Exception as e:
        print(f"An error occurred during parsing: {e}")
        return []
    
def write_card_data(cards):
    """
    Writes the card data to a CSV file.

    Args:
        cards (dict): A dictionary containing card names and their statistics.
    """
    with open(data, 'w') as file:
        file.write("card, ranking, rating, usage, usage_delta, win, win_delta, cwr\n")
        for name in cards.keys():
            rating = cards[name]['rating']
            usage = cards[name]['usage']
            usage_delta = cards[name]['usage_delta']
            win_precent = cards[name]['win_precent']
            win_delta = cards[name]['win_delta']
            cwr = cards[name]['cwr']
            file.write(f"{name},{rating},{rating},{usage},{usage_delta},{win_precent},{win_delta}, {cwr}\n")

def card_data_from_stats_royale(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = bs(response.content, 'html.parser')

        print(soup.prettify())
        

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    except Exception as e:
        print(f"An error occurred during parsing: {e}")
        return []




# want data for
# ladder
# ranked
# ultimate champion
# top 1000
# top 200
# classic challenge
# grand challenge

# can get real card stats at a latter time





