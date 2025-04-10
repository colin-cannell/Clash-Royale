import mysql.connector
import os
import pandas as pd

user = "root"
password = ""
dbName = "clashroyale"

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,  # Default MySQL port
            database=dbName,  # Replace with your database name
            user=user,     
            password=password)
        
        if conn is None:
            print("Database connection unsuccessful")
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


cards_path = "data/cards/names.txt"
# load all the cards into the database
def load_cards(path):
    cards = []
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if len(line.split(" ")) == 2:
                x, y = line.split(" ")
                name = f"{x.lower()}-{y.lower()}"
            else:
                name = line.lower()
            cards.append(name)

    conn = connect_db()
    cursor = conn.cursor()

    try:
        for card in cards:
            cursor.execute(
                "INSERT IGNORE INTO card (card_name) VALUES (%s)",
                [card]
            )
        conn.commit()
    except Exception as e:
        print(f"Error loading cards: {e}")
    finally:
        cursor.close()
        conn.close()
            
card_types = "data/trippledraft/types"
# TODO

# load tripple draft card types into the database
def load_card_types(path):
    dirs = os.listdir(path)
    for dir in dirs:
        cards = []
        table = dir.split(".")[0]
        with open(os.path.join(path, dir), 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if len(line.split(" ")) == 2:
                    x, y = line.split(" ")
                    name = f"{x.lower()}-{y.lower()}"
                else:
                    name = line.lower()
                cards.append(name)
        conn = connect_db()
        cursor = conn.cursor()
        try:
            for card in cards:
                cursor.execute(
                    f"INSERT IGNORE INTO {table} (card_name) VALUES (%s)",
                    [card]
                )
            conn.commit()
        except Exception as e:
            print(f"Error loading cards: {e}")
        finally:
            cursor.close()
            conn.close()
                

card_stats = "data/trippledraft/card_data.csv"
# load tripple draft card statiss into the database 
def load_card_stats(path):
    conn = connect_db()
    cursor = conn.cursor()


    # create the table if it doesn't exist
    ## loop through csv rows and add them to the database
    try:
        df = pd.read_csv(path)
        for i in df.iterrows():
            row = i[1]
            name = row["card"].lower()
            ranking = row["ranking"]
            rating = row["rating"]
            usage = row["usage"]    
            usage_delta = row["usage_delta"]
            win = row["win"]
            win_delta = row["win_delta"]
            cwr = row["cwr"]

            # 1. Get the card_id
            cursor.execute("SELECT card_id FROM card WHERE card_name = %s", [name])
            card_id_result = cursor.fetchone()

            if card_id_result:
                card_id = card_id_result[0]  # Extract the card_id from the result

                # 2. Insert into tripple_draft_stats using the retrieved card_id
                sql_insert = """
                    INSERT IGNORE INTO tripple_draft_stats (card_id, ranking, rating, `usage`, usage_delta, win, win_delta, cwr)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                values_insert = (card_id, ranking, rating, usage, usage_delta, win, win_delta, cwr)
                cursor.execute(sql_insert, values_insert)
            else:
                print(f"Warning: Card '{name}' not found in the 'card' table. Skipping stats insertion.")
        conn.commit()
    except Exception as e:
        print(f"Error loading card stats: {e}")
    finally:
        cursor.close()
        conn.close()
    


load_cards(cards_path)
# load_card_types(card_types)
load_card_stats(card_stats)

sequences = "data/trippleraft/sequences.txt"
def load_sequences(path):
    conn = connect_db()
    cursor = conn.cursor()

    # create the table if it doesn't exist
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            
    except Exception as e:
        print(f"Error loading sequences: {e}")
    finally:
        cursor.close()
        conn.close()

# keep track of all my friends games 
# find what decks they lose too the most
# compare them to real high rating decks
# find out what cards are the most common in those decks 
# build decks off of that

# track card predictions in draft
# track cards picked by owen