import os
import datetime

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!time' or "!t":
        try:
            dateLeave = datetime.datetime(2020, 12, 13)
            today = datetime.datetime.now()
            date_split = str(delta).split()
            date_small_split = date_split[2].split(":")
            
            msg_today = "gooooOOOOOOOOOOOOD MORRNINGGGGG VIETNAAAAAAAM!!! \n\nToday is " + today.strftime("%A") + "\n"
            msg_remaining = "There are {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds remaining until leave.".format(
                days=date_split[0],hours=date_small_split[0],minutes=date_small_split[1],seconds=round(float(date_small_split[2])))
            final_string = "".join((msg_today, msg_remaining))
            await message.channel.send(final_string)
        except:
            await message.channel.send("There was an error calculating the time remaining")

    if message.content == '!help':
        try:
            await message.channel.send("""Hello there! I am St. Bernard, a discord bot built for Company E2.\n
Try using !time or !t to get the time until leave.""")
        except:
            await message.channel.send("Something went terribly wrong")

client.run(TOKEN)