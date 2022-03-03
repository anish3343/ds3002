import requests
import json
import sys

# Read commandline input
tickers = sys.argv[1]   # sys.argv[0] contains the filename according to convention, so we ignore it

# Assemble API Call
url = "https://yfapi.net/v6/finance/quote"  # Yahoo Finance API url
querystring = {"symbols":tickers}   # List of tickers that the user wants to query
headers = {'x-api-key': "bpyjDUdr6M5vqWoxLNdxf48pFEhaxSlL7U7UyAi5"} # My API key

response = requests.request("GET", url, headers=headers, params=querystring)

stock_json = response.json()

for ticker in stock_json['quoteResponse']['result']:
    print(ticker['longName'] + ': ' + str(ticker['regularMarketPrice']))