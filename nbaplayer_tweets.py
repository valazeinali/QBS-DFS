# Pip install the command below if you don't have the development version of snscrape
# !pip install git+https://github.com/JustAnotherArchivist/snscrape.git
import snscrape
import csv
import os
import pandas as pd

with open('nba_twitter.csv', 'r') as p:
    reader = csv.reader(p)
    player_accounts_lists = [player for player in reader]
    player_accounts = [item for sublist in player_accounts_lists for item in sublist]

for player in player_accounts:
  # Using OS library to call CLI commands in Python
  # os.system(f'snscrape -f jsonl twitter-user {player} >player-tweets.json')
  # os.system(f'snscrape -f csv twitter-user {player} >player-tweets.csv')
  os.system(f'snscrape --jsonl twitter-user {player} >player-tweets.json')


  if player_accounts.index(player) == 0:
    # Reads the json generated from the CLI command above and creates a pandas dataframe
    tweets_df = pd.read_json('player-tweets.json', lines=True)
    # tweets_df = pd.read_csv('player-tweets.csv')
  else:
    tweets_df2 = pd.read_json('player-tweets.json', lines=True)
    # tweets_df2 = pd.read_csv('player-tweets.csv')
    tweets_df = tweets_df.append(tweets_df2)

# Export dataframe into a CSV
tweets_df.to_csv('nba-player-tweets.csv', sep=',', index=False)
