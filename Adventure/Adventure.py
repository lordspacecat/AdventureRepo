import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=False)
    async def beginadventure(self):
        """One path of many begins - quote from someone"""

        await self.bot.say("Protag-kun began his adventure. Protag-kun was just invited to a special party with his three friends: the upbeat baseball player Cliche-kun, the quiet and shy Yuri-chan, and the popular but sassy Bitch-sama.")

def setup(bot):
    bot.add_cog(Adventure(bot)) 
