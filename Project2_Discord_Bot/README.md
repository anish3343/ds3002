# Discord Bot

A Discord bot that sends data-driven replies to everyday questions!

## Features

This bot supports 3 unique commands:
- To get the current weather at a location, include the word "weather" and one or more locations you want weather for (defaults to Charlottesville, VA if no location specified).
    - Examples:
    - > Chicago weather
    - > What's the weather in London and Paris like today?
- To get the weather forecast for the next 7 days, include the word "weather", location(s) (defaults to Charlottesville, VA) and something like "tomorrow", "forecast" or "next Monday/Tuesday/..." in your message.
    - Examples:
    - > Chicago weather tomorrow
    - > What's the weather in London and Paris on Monday?
    - > weather in new york next week
- To get the current stock price of a company, include the word "stock" and one or more company tickers preceded by a $ and a space before any punctuation.
    - Examples:
    - > $f stock price
    - > What\'s the stock price for $aapl $ba and $msft ?
- Additionally, the bot replies with the above information when it receives a message starting with `!help`.

## Installation

### To run locally:

Requirements: Python 3.8 or higher with pip.
Using a virtual environment is highly recommended.

1. Install dependencies:
```
pip install -r requirements.txt
```
2. Run the bot:
```
python3 main.py
```

### Run from replit (recommended)

The bot is hosted on replit at https://replit.com/@anish3343/ds3002 .

## How it works

1. Current weather: The bot looks for the word "weather" in the message, then looks for city names in the message using the flashgeotext package. Then, it returns the current weather at those locations by calling the [openweathermap API](https://openweathermap.org/api).
2. 7-day weather forecast: The bot looks for the word "weather" AND a word referring to the future like "tomorrow" or "next" in the message, then looks for city names in the message using the flashgeotext package. Then, it returns the current weather at those locations by calling the [openweathermap API](https://openweathermap.org/api).
3. Stock price: The bot looks for the word "stock" in the message, then looks for stock tickers formatted like `$ABC ` with a trailing space. Then, it returns the current market price of those companies by calling the [YH Finance API](https://financeapi.net/).
