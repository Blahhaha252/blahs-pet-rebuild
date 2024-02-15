import discord
import yaml
import os
import sys
from server_settings import serversettings
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
client.load_extension("commands")
@client.event
async def on_ready():
    print("""|-------------------------|
|    bot is now online    |
|-------------------------|
|    VERSION - 0.0.001    |
|-------------------------|""")
async def commands(server, serverid, channelid, args):
    arg1 = args[0]
    arg2 = args[1] if len(args) > 1 else None
    arg3 = args[2] if len(args) > 2 else None
    print(arg1, arg2, arg3)
    arg1 = arg1[1:]
    channel = client.get_channel(channelid)
    if arg1 in ['watched', 'watch_list'] and arg2 and arg3 is None:
        watch_list = server.watched_list()
        await channel.send(watch_list)
    if arg1 
@client.event 
async def on_message(message):
    serverid = message.guild.id
    args = message.content.split()
    channelid = message.channel.id
    arg1 = args[0]
    server = serversettings(serverid=serverid)
    prefix = serversettings.prefix(server)
    if arg1.startswith(prefix):
        await commands(server, serverid, channelid, args)
client.run(BOTTOKEN)