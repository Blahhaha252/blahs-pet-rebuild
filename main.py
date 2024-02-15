import discord
import yaml
import os
import sys
from server_settings import serversettings
from commands import sscommands
from datetime import datetime, timezone
from discord.ext import commands
with open('config.yml', 'r') as file:
    data = yaml.safe_load(file)
    BOTTOKEN = data['bot']['token']
    prefix = data['bot']['prefix']
    
intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Add this line to enable the messages intent
client = commands.Bot(command_prefix=prefix, intents=intents)
client.load_extension("sscommands")
@client.event
async def on_ready():
    print("""|-------------------------|
|    bot is now online    |
|-------------------------|
|    VERSION - 0.0.001    |
|-------------------------|""")

@client.event 
async def on_message(message):
    serverid = message.guild.id
    args = message.content.split()
    channelid = message.channel.id
    arg1 = args[0]
    print(message.content)
    print(args)
    print(arg1)
    server = serversettings(serverid=serverid)
    prefix = server.prefix()
    isowner = False
    if message.guild and message.author.id == message.guild.owner_id:
        isowner = True
    if arg1.startswith(prefix):
        await sscommands(client, server, serverid, channelid, args, isowner)
client.run(BOTTOKEN)