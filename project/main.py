# fukurou

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user.name} is live!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send("Hi! I'm Fukurou")

client.run(TOKEN)
