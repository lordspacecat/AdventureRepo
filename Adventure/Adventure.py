import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    async def punch(self, role:discord.Role):
        """I will punch anyone! >.<"""
        
        answer = await self.bot.wait_for_message(timeout=120, author=author)
        if answer not in discord.Role:
            await self.bot.say("Timed out, canceling")
    
        await self.bot.say("You punched!")

    @commands.command(no_pm=False)
    async def beginadventure(self):
        """One path of many begins - quote from someone"""

        await self.bot.say("Protag-kun began his adventure. \nIf you are 'Ticketed', you may proceed.")

def setup(bot):
    bot.add_cog(Adventure(bot)) 
