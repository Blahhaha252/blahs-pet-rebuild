import discord
import yaml
import os
import sys
import re
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
#detects if message author is owner
    if message.guild and message.author.id == message.guild.owner_id:
        isowner = True
#detecting if message has prefix
    if arg1.startswith(prefix):
        await sscommands(client, server, serverid, channelid, args, isowner)
#auto hidden link detection system (needs to be updated)
    pattern = r'\[(.*?)\]\((.*?)\)'
    match = re.search(pattern, message.content)
    if match:
        extracted_text = match.group(1)
        extracted_link = match.group(2)
        await message.reply(f"!WARNING HIDDEN URL!\nTEXT: {extracted_text}\nURL: {extracted_link}")
# some logic to help with discord SRV compatibility
#    pattern2 = r'\[([^]]+)\]([^ ]*) »\s*(.*)'
#    match = re.match(pattern2, message.content)
#    if match:
#        group_brackets = match.group(1)
#        information = match.group(2)
#        after_arrow = match.group(3)
#        print("match found", group_brackets, information, after_arrow)
#    else:
#        print("match not found")
client.run(BOTTOKEN)
