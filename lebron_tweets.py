# Pip install the command below if you don't have the development version of snscrape
import snscrape
import pandas as pd
import os

# Using OS library to call CLI commands in Python
os.system(f'snscrape --jsonl twitter-user kingjames >lebron.json')

# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df = pd.read_json('lebron.json', lines=True)

# Export dataframe into a CSV
tweets_df.to_csv('lebron-tweets.csv', sep=',', index=False)
