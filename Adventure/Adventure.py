import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def contextcom(self, ctx):
        """haha faggot"""
        
        name = ctx.message.author.name
        await self.bot.say(name)
        and self.bot.say("began his adventure.")
        
    @commands.command(pass_context=True)
    async def beginadventure(self, ctx):
        """One path of many begins - quote from someone"""
        
        name = ctx.message.author.name
        await self.bot.say(name)
        await self.bot.say("began his adventure. \nIf you are 'Ticketed you may continue.")
   

def setup(bot):
    bot.add_cog(Adventure(bot)) 
