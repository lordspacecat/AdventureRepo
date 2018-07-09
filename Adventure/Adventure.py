import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(no_pm=False, pass_context=True)
    async def beginadventure(self, ctx):
        """Begin your adventure."""
        
        user = ctx.message.author.name
        await self.bot.say("" + user + " must make a choice. \nIn order to survive, " + user + " must kill person 1 or person 2")
            
        answer = await self.bot.wait_for_message(timeout=10)
        
        if no answer:
            await self.bot.say("Time's up, " + user + " . Due to your indecisiveness, both Person 1 and Person 2 shall die.")
        
        
def setup(bot):
    bot.add_cog(Adventure(bot)) 
