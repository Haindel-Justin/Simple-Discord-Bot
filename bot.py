import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await member.add_roles(role)

@client.event
async def on_member_join(member):
    guild = client.get_guild(608418023748927508);
    for role in guild.roles:
        if (role.name == 'Default'):
            default_role = role
    await member.add_roles(default_role)

client.run('KEY')
