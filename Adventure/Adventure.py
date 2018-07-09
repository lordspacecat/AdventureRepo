import discord
from discord.ext import commands

class Adventure:
    """This is a cog"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=False, pass_context=True)
    async def beginadventure(self, ctx):
        """Begin your adventure."""

        await self.bot.say("You must make a choice. \nIn order to survive, you must kill person 1 or person 2")
        
        user = ctx.message.author.name
        answer = await self.bot.wait_for_message(timeout=10)
        
            if answer:
                await self.bot.say("Time's up, " + user + " . Due to your indecisiveness, both Person 1 and Person 2 shall die.")
                return
        
        
def setup(bot):
    bot.add_cog(Adventure(bot)) 
