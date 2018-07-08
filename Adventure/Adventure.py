import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    async def punch(self, role : discord.Role):
        """I will punch anyone! >.<"""

        await self.bot.say("You punched!")

    @commands.command(no_pm=False)
    async def beginadventure(self):
        """One path of many begins - quote from someone"""

        await self.bot.say("Protag-kun began his adventure. \nIf you are 'Ticketed', you may proceed.")

def setup(bot):
    bot.add_cog(Adventure(bot)) 
