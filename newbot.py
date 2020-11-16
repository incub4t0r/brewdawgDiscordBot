#importing the discord module
import discord, datetime, os
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#creating a new discord client for us to use. cool_bot be the client
Client=discord.Client()
bot = commands.Bot(command_prefix = '!')
#methods waiting for the event
@bot.event
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(bot.user.name)
    print("Userid: ",end='')
    print(bot.user.id)


class Bonker(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)
@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)
async def slap(ctx, *, reason: Bonker):
    await ctx.send(reason)

bot.run(TOKEN)