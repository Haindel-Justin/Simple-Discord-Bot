import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

client.run('NjA4NDIwODM0NjgzMzg3OTQ0.XUocEA.lbFEGHgB08aWWLTaKGFv0hR7KCY')
