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
            future_words = ["TOMORROW", "NEXT", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            if any(word in content for word in future_words):
                today = False
            # Make a call to the weather API with the lat and lon:
            weather_query_string = "https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&appid={2}&units=imperial".format(lat, lon, os.environ['WEATHER'])
            # Load the response into an object
            weather_response = requests.get(weather_query_string).json()
            # Construct the weather response by compiling current time at location temperature, feels like temperature, current conditions as well as high and low temps for the day
            time_dt = datetime.datetime.utcfromtimestamp(weather_response['current']['dt'] + weather_response['timezone_offset'])
            time = time_dt.strftime("%-I:%M %p, %A %-d %B %Y")
            temp = round(weather_response['current']['temp'])
            feels_like = round(weather_response['current']['feels_like'])
            conditions = weather_response['current']['weather'][0]['description'].title()
            day_min = round(weather_response['daily'][0]['temp']['min'])
            day_max = round(weather_response['daily'][0]['temp']['max'])
            weather_string = "Current Time: {0}\nTemperature: **{1}°F** *(Feels like {2}°F)*\nConditions: **{3}**\nToday: **Min {4}°F, Max {5}°F**".format(time, temp, feels_like, conditions, day_min, day_max)
            # Send the weather response
            await message.channel.send("Here's the weather in {0}, {1}{2} :flag_{3}: :\n{4}".format(city, state, country, country.lower(), weather_string))
        

client.run(os.getenv('TOKEN'))