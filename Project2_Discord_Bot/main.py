import discord
import os
from dotenv import load_dotenv
import geograpy
import requests
import datetime

load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged into {1} as {0.user}'.format(client, "XXXSERVER"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.upper()

    if content.startswith('HELLO'):
        await message.channel.send('Hello!')

    if content.startswith('$HELP'):
        help_string = 'Hello! Thanks for using DS3002-Helper-Bot! Here\'s some things I can do:\n- To get the current weather at a location, include the word "weather" and the location you want weather for (defaults to Charlottesville, VA if no location specified).\n- To get the weather forecast for the next 7 days, include the word "weather", location (defaults to Charlottesville, VA) and something like "tomorrow", "forecast" or "next Monday/Tuesday/..." in your message.'
        await message.channel.send(help_string)

    # Get weather
    if 'WEATHER' in content:
        # Look for city names
        places = geograpy.get_geoPlace_context(text=content.title())
        # If no city was found, default to Charlottesville
        if not places.cities:
            await message.channel.send("Hmm. Either you didn't specify a city, or I couldn't find the city you entered.")
            places = geograpy.get_geoPlace_context(text="Charlottesville")
        # Get the weather at each city
        for city in places.cities:
            # Make a call to the geolocation API with the city name
            city_query_string = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&appid=" + os.environ['WEATHER']
            # Load the response into an object
            city_response = requests.get(city_query_string).json()
            # Get City, State, Country, lat and long from the API response
            city = city_response[0]['name']
            state = ""
            if "state" in city_response[0]:
                state = city_response[0]['state'] + ", "
            country = city_response[0]['country']
            lat = city_response[0]['lat']
            lon = city_response[0]['lon']
            # Figure out whether we want to get today's weather or future days' weather (i.e. 5-day forecast)
            today = True
            future_words = ["TOMORROW", "NEXT", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", "FORECAST"]
            if any(word in content for word in future_words):
                today = False
            # Make a call to the weather API with the lat and lon:
            weather_query_string = "https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&appid={2}&units=imperial".format(lat, lon, os.environ['WEATHER'])
            # Load the response into an object
            weather_response = requests.get(weather_query_string).json()
            # If the user did not want future weather, send today's weather
            if today:
                # Construct the weather response by compiling current time at location temperature, feels like temperature, current conditions as well as high and low temps for the day
                time_dt = datetime.datetime.utcfromtimestamp(weather_response['current']['dt'] + weather_response['timezone_offset'])
                time = time_dt.strftime("%-I:%M %p, %A %-d %B %Y")
                temp = round(weather_response['current']['temp'])
                feels_like = round(weather_response['current']['feels_like'])
                conditions = weather_response['current']['weather'][0]['description'].title()
                day_min = round(weather_response['daily'][0]['temp']['min'])
                day_max = round(weather_response['daily'][0]['temp']['max'])
                weather_string = "Current Time: {0}\n\nTemperature: **{1}°F** *(Feels like {2}°F)*\n\nConditions: **{3}**\n\nToday: **Min {4}°F, Max {5}°F**".format(time, temp, feels_like, conditions, day_min, day_max)
                # Send the weather response
                await message.channel.send("Here's the weather in {0}, {1}{2} :flag_{3}: :\n{4}".format(city, state, country, country.lower(), weather_string))
            # If the user requested future weather, send that instead
            else:
                # Construct the weather response by compiling date, conditions, min and max temps for each day
                days_forecast = ""
                for day in weather_response['daily']:
                    day_dt = datetime.datetime.utcfromtimestamp(day['dt'] + weather_response['timezone_offset'])
                    day_date = day_dt.strftime("%a %-d %b")
                    cond = day['weather'][0]['description'].title()
                    min_temp = str(round(day['temp']['min']))
                    max_temp = str(round(day['temp']['max']))
                    day_summary = "{0} : {1}, Min: {2}°F, Max: {3}°F\n\n".format(day_date, cond, min_temp, max_temp)
                    days_forecast += day_summary
                await message.channel.send("Here's the forecast for {0}, {1}{2} :flag_{3}: for the next week:\n\n{4}".format(city, state, country, country.lower(), days_forecast))

    # Get stocks
    if 'STOCK' in content:
        await message.channel.send("Here's the stocks you requested:")

client.run(os.getenv('TOKEN'))