#importing the discord module
import discord, datetime, os, random, json
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

bot = commands.Bot(command_prefix="!")

# Prepares bot with balance system
@bot.event
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(bot.user.name)
    global brewbucks
    try:
        with open(os.path.join(file_location, 'brewbucks.json')) as f:
            brewbucks = json.load(f)
    except:
        print("Could not load brewbucks.json")
        brewbucks = {}

### BALANCE SYSTEM START ###
@bot.command()
async def balance(ctx):
    id = str(ctx.message.author.id)
    if id in brewbucks:
        await ctx.send("You have {} brewbucks".format(brewbucks[id]))
    else:
        await ctx.send("You do not have an account")

@bot.command()
async def register(ctx):
    id = str(ctx.message.author.id)
    if id not in brewbucks:
        brewbucks[id] = 100
        await ctx.send("You are now registered")
        _save()
    else:
        await ctx.send("You already have an account")

@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    primary_id = str(ctx.message.author.id)
    other_id = str(other.id)
    if primary_id not in brewbucks:
        await ctx.send("You do not have an account")
    elif other_id not in brewbucks:
        await ctx.send("The other party does not have an account")
    elif brewbucks[primary_id] < amount:
        await ctx.send("You cannot afford this transaction")
    else:
        brewbucks[primary_id] -= amount
        brewbucks[other_id] += amount
        await ctx.send("Transaction complete")
    _save()

def _save():
    with open(os.path.join(file_location, 'brewbucks.json'), 'w+') as f:
        json.dump(brewbucks, f)

@bot.command()
async def save(ctx):
    _save()

#https://stackoverflow.com/questions/55485988/discord-money-bot-keeping-user-ids-in-json-file-when-bot-restarts-it-creats-a
### BALANCE SYSTEM END ###

### COMMANDS START ###

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
    
@bot.command(
    help = "Calculates using datetime the amount of time remaining until graduation",
    brief = "Prints time until graduation '23")
async def graduation(ctx):
    dateLeave = datetime.datetime(2023, 5, 27)
    today = datetime.datetime.now()
    delta = dateLeave-today
    date_split = str(delta).split()
    date_small_split = date_split[2].split(":")
    
    msg_today = "Hello Brewdawg. \n\nToday is " + today.strftime("%A") + ".\n"
    msg_remaining = "For the Class of 2023, there are `{days}` days, `{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds remaining until graduation.".format(
        days=date_split[0],hours=date_small_split[0],minutes=date_small_split[1],seconds=round(float(date_small_split[2])))
    final_string = "".join((msg_today, msg_remaining))
    emb = discord.Embed(title=None, description=final_string)
    await ctx.send(embed=emb)

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

@bot.command()
async def godawgs(ctx):
    final_string = ""
    art = open(os.path.join(file_location, 'brewdawg.txt'))
    for line in art:
        final_string += line
    await ctx.send(f"```{final_string}```")

bot.run(TOKEN)

#https://stackoverflow.com/questions/63625197/how-to-make-a-currency-system-in-discord-py

#TODO
# add a brewbuck system
# add exception handling
# add a bonk tracker
# add a !source to give a link to the github it is hosted on
