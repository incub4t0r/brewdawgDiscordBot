#importing the discord module
import discord, datetime, os, random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(bot.user.name)

@bot.command(
    help = "Utilizes 1337 coding to determine correct response and latency",
    brief = "Prints pong and latency"
)
async def ping(ctx):
    final_string = 'Pong! {0}'.format(bot.latency)
    emb = discord.Embed(title=None, description=final_string)
    await ctx.send(embed=emb)

@bot.command(
    help = "Parses using a for loop an entire message and returns it",
    brief = "Prints your message back"
)
async def echo(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    await ctx.send(response)

@bot.command(
    help = "Calculates using datetime the amount of time remaining until leave",
    brief = "Prints time until leave")
async def countdown(ctx):
    dateLeave = datetime.datetime(2020, 12, 13)
    today = datetime.datetime.now()
    delta = dateLeave-today
    date_split = str(delta).split()
    date_small_split = date_split[2].split(":")
    
    msg_today = "gooooOOOOOOOOOOO BREEEEWWWWDAAAWWWWWGGSSSS!!! \n\nToday is " + today.strftime("%A") + ".\n"
    msg_remaining = "There are `{days}` days, `{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds remaining until leave.".format(
        days=date_split[0],hours=date_small_split[0],minutes=date_small_split[1],seconds=round(float(date_small_split[2])))
    final_string = "".join((msg_today, msg_remaining))
    emb = discord.Embed(title=None, description=final_string)
    await ctx.send(embed=emb)

#@bot.command()
#async def bonk(ctx,member_id:int):
    #author = ctx.author
#    member = ctx.guild.get_member(member_id)
#    print (member)
#    final_string = f"{ctx.author.mention} bonked {member.mention}"
    #final_string = "{author} slapped {member}!".format(
    #    author=ctx.author.mention, member=member.mention)
#    await ctx.send(final_string)

@bot.command(
    help="Send someone to horny jail",
    brief="Send someone to horny jail"
)
async def bonk(ctx, members: commands.Greedy[discord.Member]):
    slapped = ", ".join(x.name for x in members)
    #author = ctx.author
    await ctx.send('{} just got bonked!'.format(slapped))

@bot.command(
    help="Sends out a loud and thunderous 'go dawgs' to notify everyone",
    brief="Call everyone with a reason"
)
async def callsign(ctx,*,reason):
    author = ctx.author.mention
    final_string = f"{author} calls {'@everyone'}! Reason: {reason}"
    await ctx.send(final_string)
#https://stackoverflow.com/questions/64028189/discord-ext-commands-errors-missingrequiredargument-user-is-a-required-argument
bot.run(TOKEN)