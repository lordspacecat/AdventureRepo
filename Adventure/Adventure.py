import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(no_pm=False, pass_context=True)
    async def oregontrail(self, ctx):
        """Begin the Oregon Trail."""
        
        user = ctx.message.author.name
        await self.bot.say("" + user + " began the Oregon Trail. \n Many kinds of people made the trip to Oregon. \nYou may: \n!banker - Be a banker from Boston \n!carpenter - Be a carpenter from Ohio \n!farmer - Be a farmer from Illinois")
        
        
def setup(bot):
    bot.add_cog(Adventure(bot)) 
