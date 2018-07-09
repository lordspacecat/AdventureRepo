import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(no_pm=False, pass_context=True, timeout=10)
    async def beginadventure(self, ctx):
        """Begin your adventure."""
        
        user = ctx.message.author.name
        answer = await self.bot.wait_for_message(timeout=120, user=user)
        
        if not answer:
            await self.bot.say("Time's up, " + user + " . Due to your indecisiveness, both Person 1 and Person 2 shall die.")
            
        await self.bot.say("" + user + " must make a choice. \nIn order to survive, " + user + " must kill person 1 or person 2")
        
        
def setup(bot):
    bot.add_cog(Adventure(bot)) 
