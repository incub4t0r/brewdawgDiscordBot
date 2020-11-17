from discord.ext import commands
import discord, datetime, os, random, json

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#def calc_delta(dateLeave):
#    today = datetime.datetime.now()
#    delta = dateLeave-today
#    return (delta)

def send_msg(msg):
        emb = discord.Embed(title=None, description=msg,color=0x957530)
        return emb

class Countdown(commands.Cog):
    def __init(self, bot):
        self.bot = bot
    
    @commands.command(
        help = "Calculates using datetime the amount of time remaining until winter leave",
        brief = "Prints time until winter leave"
    )
    async def leave(self, ctx):
        dateLeave = datetime.datetime(2020, 12, 13)
        today = datetime.datetime.now()
        delta = dateLeave-today
        date_split = str(delta).split()
        date_small_split = date_split[2].split(":")
        
        msg_today = "gooooOOOOOOOOOOO BREEEEWWWWDAAAWWWWWGGSSSS!!!\n\nToday is " + today.strftime("%A") + ".\n"
        msg_remaining = "There are `{days}` days, `{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds remaining until leave.".format(
            days=date_split[0],hours=date_small_split[0],minutes=date_small_split[1],seconds=round(float(date_small_split[2])))
        resp = "".join((msg_today, msg_remaining))
        await ctx.send(embed = send_msg(resp))

    @commands.command(aliases=['graduation'],
        help = "Calculates using datetime the amount of time remaining until graduation",
        brief = "Prints time until graduation '23"
    )
    async def grad(self, ctx):
        dateLeave = datetime.datetime(2023, 5, 27)
        today = datetime.datetime.now()
        delta = dateLeave-today
        date_split = str(delta).split()
        date_small_split = date_split[2].split(":")
        
        msg_today = "Henlo. \n\nToday is " + today.strftime("%A") + ".\n"
        msg_remaining = "For the Class of 2023, there are `{days}` days, `{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds remaining until graduation.".format(
            days=date_split[0],hours=date_small_split[0],minutes=date_small_split[1],seconds=round(float(date_small_split[2])))
        resp = "".join((msg_today, msg_remaining))
        await ctx.send(embed = send_msg(resp))

def setup(bot):
    bot.add_cog(Countdown(bot))