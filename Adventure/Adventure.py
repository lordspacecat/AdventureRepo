import discord
from discord.ext import commands

class Adventure:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)
    async def beginadventure(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("user.mention began his adventure.")

def setup(bot):
    bot.add_cog(Adventure(bot)) 
