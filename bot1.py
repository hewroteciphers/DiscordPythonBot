#!/usr/bin/python3
# bot1.py
#
# see https://realpython.com/how-to-make-a-discord-bot-python/
#
# prerequisites:
#   pip3 install discord python-dotenv

import os
import discord
from dotenv import load_dotenv

# get token ids from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


# create the bot
client = discord.Client()

@ client.event
async def on_ready():
    #print(f'{client.user} has connected to Discord!')
    #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    guild = discord.utils.get(client.guilds, name == GUILD)
    #for guild in client.guilds:
    #    if guild.name == GUILD:
    #        break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run(TOKEN)
