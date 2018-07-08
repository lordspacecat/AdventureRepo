import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    async def punch(self, role:discord.Role):
        """I will punch anyone! >.<"""
        
        await self.bot.say("You punched!")

    @commands.command(no_pm=False)
    async def beginadventure(self, ctx):
        """One path of many begins - quote from someone"""
        
        name = ctx.message.author.name
        await self.bot.say("(name) began his adventure. \nIf you are 'Ticketed', you may proceed.")
        
    @commands.command(no_pm=False)
    async def 

def setup(bot):
    bot.add_cog(Adventure(bot)) 
