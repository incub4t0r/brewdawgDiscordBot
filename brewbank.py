from discord.ext import commands
import discord, datetime, os, random, json

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

global brewbucks
try:
    with open(os.path.join(file_location, 'brewbucks.json')) as f:
        brewbucks = json.load(f)
    print("Loaded brewbucks.json")
except:
    print("Could not load brewbucks.json")
    brewbucks = {}

def _save():
        with open(os.path.join(file_location, 'brewbucks.json'), 'w+') as f:
            json.dump(brewbucks, f)

def send_msg(msg):
        emb = discord.Embed(title=None, description=msg,color=0x63B1FF)
        return emb

class Brewbank(commands.Cog):
    def __init(self, bot):
        self.bot = bot

    @commands.command(
        help = "Check your brewbuck balance",
        brief = "Check your brewbuck balance"
    )
    async def balance(self, ctx):
        id = str(ctx.message.author.id)
        if id in brewbucks:
            resp = ("You have {} brewbucks".format(brewbucks[id]))
        else:
            resp = ("You do not have an account")
        await ctx.send(embed = send_msg(resp))


    @commands.command(
        help = "Register for a brewbuck account",
        brief = "Register for a brewbuck account"
    )
    async def register(self, ctx):
        id = str(ctx.message.author.id)
        if id not in brewbucks:
            brewbucks[id] = 100
            resp = ("You are now registered")
            _save()
        else:
            resp = ("You already have an account")
        await ctx.send(embed = send_msg(resp))

    @commands.command(
        help = "Transfer brewbucks to another user",
        brief = "Send brewbucks to other user",
        pass_context=True)
    async def transfer(self, ctx, amount: int, other: discord.Member):
        primary_id = str(ctx.message.author.id)
        other_id = str(other.id)
        if primary_id not in brewbucks:
            resp = ("You do not have an account")
        elif other_id not in brewbucks:
            resp = ("The other party does not have an account")
        elif brewbucks[primary_id] < amount:
            resp = ("You cannot afford this transaction")
        else:
            brewbucks[primary_id] -= amount
            brewbucks[other_id] += amount
            resp = ("Transaction complete")
        await ctx.send(embed = send_msg(resp))
        _save()

    @commands.command(
        help = "Force the bot to save brewbuck amounts",
        brief = "Force bot to save bank"
    )
    async def save(self, ctx):
        _save()

    #https://stackoverflow.com/questions/55485988/discord-money-bot-keeping-user-ids-in-json-file-when-bot-restarts-it-creats-a
    #https://stackoverflow.com/questions/49788888/python-discord-bot-event-not-working/49789727#49789727
    #https://stackoverflow.com/questions/63625197/how-to-make-a-currency-system-in-discord-py
    #https://stackoverflow.com/questions/64028189/discord-ext-commands-errors-missingrequiredargument-user-is-a-required-argument


def setup(bot):
    bot.add_cog(Brewbank(bot))