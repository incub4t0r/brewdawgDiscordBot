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

class Brewbank(commands.Cog):
    def __init(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        id = str(ctx.message.author.id)
        if id in brewbucks:
            await ctx.send("You have {} brewbucks".format(brewbucks[id]))
        else:
            await ctx.send("You do not have an account")

    @commands.command()
    async def register(self, ctx):
        id = str(ctx.message.author.id)
        if id not in brewbucks:
            brewbucks[id] = 100
            await ctx.send("You are now registered")
            _save()
        else:
            await ctx.send("You already have an account")

    @commands.command(pass_context=True)
    async def transfer(self, ctx, amount: int, other: discord.Member):
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

    @commands.command()
    async def save(self, ctx):
        _save()

    #https://stackoverflow.com/questions/55485988/discord-money-bot-keeping-user-ids-in-json-file-when-bot-restarts-it-creats-a
    #https://stackoverflow.com/questions/49788888/python-discord-bot-event-not-working/49789727#49789727
    #https://stackoverflow.com/questions/63625197/how-to-make-a-currency-system-in-discord-py
    #https://stackoverflow.com/questions/64028189/discord-ext-commands-errors-missingrequiredargument-user-is-a-required-argument


def setup(bot):
    bot.add_cog(Brewbank(bot))