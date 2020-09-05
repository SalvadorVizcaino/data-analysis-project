import csv
import pandas as pd
import requests
import io

# CONSTANTS
FILENAME = 'http://galileoguzman.com/data/covid19_tweets.csv'
s=requests.get(FILENAME).content
dfcovid = pd.read_csv(io.StringIO(s.decode('utf-8')))


print(dfcovid.head())


