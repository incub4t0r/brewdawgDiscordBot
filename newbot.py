#importing the discord module
import discord, datetime, os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#creating a new discord client for us to use. cool_bot be the client
client=discord.Client()
#methods waiting for the event
@client.event
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(client.user.name)
    print("Userid: ",end='')
    print(client.user.id)
@client.event

#when the bot gets the message this method gets triggered
async def on_message(message):
    if message.author.id == client.user.id:
        return
    #message starts with hi or hello then print these
    if message.content.startswith('!h'):
        await message.channel.send("""Hello there! I am St. Bernard, a discord bot built for Company E2.\n
Try using !time or !t to get the time until leave.""")
    elif message.content.startswith('!t'):
        dateLeave = datetime.datetime(2020, 12, 13)
        today = datetime.datetime.now()
        delta = dateLeave-today
        date_split = str(delta).split()
        date_small_split = date_split[2].split(":")
        
        msg_today = "gooooOOOOOOOOOOOOD MORRNINGGGGG VIETNAAAAAAAM!!! \n\nToday is " + today.strftime("%A") + "\n"
        msg_remaining = "There are {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds remaining until leave.".format(
            days=date_split[0],hours=date_small_split[0],minutes=date_small_split[1],seconds=round(float(date_small_split[2])))
        final_string = "".join((msg_today, msg_remaining))
        await message.channel.send(final_string)

client.run(TOKEN)