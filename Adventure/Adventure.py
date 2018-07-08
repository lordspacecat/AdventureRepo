import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
    @ccrole.command(name="add", pass_context=True)
    @checks.mod_or_permissions(administrator=True)
    async def ccrole_add(self, ctx, command: str):

        
        await self.bot.say('What roles should it add? (Must be comma separated)\nSay `None` to skip adding roles')

        answer = await self.bot.wait_for_message(timeout=999, author=author)
        if not answer:
            await self.bot.say("Timed out, canceling")
            return
        arole_list = ["Test Role"]
        if answer.content.upper() != "NONE":
            arole_list = answer.content.split(",")

            try:
                arole_list = [discord.utils.get(server.roles, name=role.strip('Test Role')).id for role in arole_list]
            except:
                await self.bot.say("Invalid answer, canceling")
return
    
    @commands.command()
    async def punch(self, user : discord.Member):
        """I will punch anyone! >.<"""

        await self.bot.say("You punched " + user.mention + "!")

    @commands.command(no_pm=False)
    async def beginadventure(self):
        """One path of many begins - quote from someone"""

        await self.bot.say("Protag-kun began his adventure. \nIf you are 'Ticketed', you may proceed.")

def setup(bot):
    bot.add_cog(Adventure(bot)) 
