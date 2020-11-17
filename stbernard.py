#importing the discord module
import discord, datetime, os, random, json
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

bot = commands.Bot(command_prefix="!")

# Attempts to load the extensions from brewbank and countdown
try:
    bot.load_extension('brewbank')
    print("Loaded brewbank.py")
except:
    print("Error loading brewbank, brewbank.py not found")

try:
    bot.load_extension('countdown')
    print("Loaded countdown.py")
except:
    print("Error loading countdown, countdown.py not found")

# Logs in bot
@bot.event
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name="West Point"))
    #https://stackoverflow.com/questions/59126137/how-to-change-discord-py-bot-activity

### COMMANDS START ###

def send_msg(msg):
    emb = discord.Embed(title=None, description=msg,color=0x957530)
    return emb

@bot.command(
    help = "Utilizes 1337 coding to determine correct response and latency",
    brief = "Prints pong and latency"
)
async def ping(ctx):
    resp = 'Pong! {0}'.format(bot.latency)
    await ctx.send(embed = send_msg(resp))

@bot.command(
    help = "Parses using a for loop an entire message and returns it",
    brief = "Prints your message back"
)
async def echo(ctx, *args):
    resp = ""
    for arg in args:
        resp = resp + " " + arg
    await ctx.send(embed = send_msg(resp))

@bot.command(
    help="Send someone to horny jail",
    brief="Send someone to horny jail"
)
async def bonk(ctx, members: commands.Greedy[discord.Member]):
    bonked = ", ".join(x.name for x in members)
    #author = ctx.author

    resp = '{} just got bonked!'.format(bonked)
    await ctx.send(embed = send_msg(resp))

@bot.command(
    help="Sends out a loud and thunderous 'go dawgs' to notify everyone",
    brief="Call everyone with a reason"
)
async def roar(ctx,*,reason):
    author = ctx.author.mention
    resp = f"{author} calls {'@everyone'}! Reason: {reason}"
    await ctx.send(resp)
    #await ctx.send(embed = send_msg(resp))
#https://stackoverflow.com/questions/64028189/discord-ext-commands-errors-missingrequiredargument-user-is-a-required-argument

@bot.command(
    help="You know what this does",
    brief="You know what this does"
)
async def godawgs(ctx):
    resp = f"{'@everyone'} go dawgs"
    #art = open(os.path.join(file_location, 'brewdawg.txt'))
    #for line in art:
    #    resp += line
    await ctx.send(resp)

@bot.command(
    help="Provides the github source for the bot",
    brief="See the code"
)
async def source(ctx):
    resp = 'https://github.com/incub4t0r/brewdawgDiscordBot'
    await ctx.send(embed = send_msg(resp))

bot.run(TOKEN)


#TODO
# add a brewbuck system --- done
# add a bark or bite system to add/take away balance
# add exception handling
# add a bonk tracker
# add a !source to give a link to the github it is hosted on
