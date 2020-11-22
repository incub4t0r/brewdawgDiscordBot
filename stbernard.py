### IMPORTS ###
import discord, datetime, os, random, json, asyncio
from dotenv import load_dotenv
from discord.ext import commands, tasks

### LOADING VAR/ENV ###
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

bot = commands.Bot(command_prefix=">")

# Attempts to load the extensions from brewbank, countdown, and bonktracker
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
try:
    bot.load_extension('bonktracker')
    print("Loaded bonktracker.py")
except:
    print("Error loading bonktracker, bonktracker.py not found")

# Logs in bot
@bot.event
async def on_ready():
    global reply
    print('Logged in')
    print(f"Username: {bot.user.name}")
    print('-----')
    await bot.change_presence(activity=discord.Game(name="Listening in st-bernard"))
    reply = bot.get_channel(779854850963537981)

    #https://stackoverflow.com/questions/59126137/how-to-change-discord-py-bot-activity

### DEFINED FUNCTIONS ###

# Checks to ensure bot commands are being issued in correct place
# def in_channel(channel_id):
#     def predicate(ctx):
#         return ctx.message.channel.id == channel_id
#     return commands.check(predicate)

# Easy send message function
def send_msg(msg):
    emb = discord.Embed(title=None, description=msg,color=0x957530)
    return emb

# Returns time until leave
def calc_leave():
    dateLeave = datetime.datetime(2020, 12, 13)
    today = datetime.datetime.now()
    delta = dateLeave-today
    date_split = str(delta).split()
    date_small_split = date_split[2].split(":")
    msg_today = "ITS A NEW DAY!!!\n\nToday is " + today.strftime("%A") + ".\n"
    msg_remaining = "There are `{days}` days, `{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds remaining until leave.".format(
        days=date_split[0],hours=date_small_split[0],minutes=date_small_split[1],seconds=round(float(date_small_split[2])))
    resp = "".join((msg_today, msg_remaining))
    return resp

### DEFINED COMMANDS ###

@bot.command(
    help = "Utilizes 1337 coding to determine correct response and latency",
    brief = "Prints pong and latency"
)
async def ping(ctx):
    resp = f'Pong! {bot.latency}'
    await reply.send(embed = send_msg(resp))

@bot.command(
    help = "Parses using a for loop an entire message and returns it",
    brief = "Prints your message back"
)
async def echo(ctx, *args):
    resp = ""
    for arg in args:
        resp = resp + " " + arg
    await reply.send(embed = send_msg(resp))

@bot.command(
    help="Sends out a loud and thunderous 'go dawgs' to notify everyone",
    brief="Call everyone with a reason"
)
async def roar(ctx,*,reason):
    author = ctx.author.mention
    resp = f"{author} calls {'@everyone'}! Reason: {reason}"
    await reply.send(resp)

#https://stackoverflow.com/questions/64028189/discord-ext-commands-errors-missingrequiredargument-user-is-a-required-argument

@bot.command(
    help="You know what this does",
    brief="You know what this does"
)
async def godawgs(ctx):
    resp = f"{'@everyone'} go dawgs"
    await reply.send(resp)

@bot.command(
    help="Provides the github source for the bot",
    brief="See the code"
)
async def source(ctx):
    resp = 'Created by 43y3s.\nhttps://github.com/incub4t0r/brewdawgDiscordBot'
    await reply.send(embed = send_msg(resp))

@tasks.loop(minutes=1)
async def check_new_day():
    await bot.wait_until_ready()
    today = datetime.datetime.now()
    if (int(str(today).split()[1].split(":")[0])==7 and int(str(today).split()[1].split(":")[1])==0):
        resp = calc_leave()
        await reply.send(embed = send_msg(resp))
        await asyncio.sleep(65)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await reply.send(embed = send_msg("No such command, use !help to view commands"))
    else:
        raise error


check_new_day.start()
bot.run(TOKEN)


#TODO
# add a brewbuck system --- done
# add exception handling --- partial
# add a bonk tracker --- done
# add a !source to give a link to the github it is hosted on --- done
# change the @everyone to be unembedded --- done
# add a bark or bite system to add/take away balance

#https://imgur.com/a/2aM6AnD dm function