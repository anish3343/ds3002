import discord
import os
from dotenv import load_dotenv

load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged into {1} as {0.user}'.format(client, "XXXSERVER"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))