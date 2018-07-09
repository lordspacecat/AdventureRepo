import discord
from discord.ext import commands

class Adventure:
    """A generic name for a generic story."""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(pass_context=True, no_pm=True)
    async def ccrole(self, ctx):
        """Custom commands management"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @ccrole.command(name="add", pass_context=True)
    @checks.mod_or_permissions(administrator=True)
    async def ccrole_add(self, ctx, command: str):
        """Adds a custom command with roles"""
        command = command.lower()
        if command in self.bot.commands:
            await self.bot.say("That command is already a standard command.")
            return

        server = ctx.message.server
        author = ctx.message.author

        if server.id not in self.c_commands:
            self.c_commands[server.id] = {}
        cmdlist = self.c_commands[server.id]
        if command in cmdlist:
            await self.bot.say("This command already exists. Delete"
                               "`it with {}ccrole delete` first."
                               "".format(ctx.prefix))
            return

        # Roles to add
        await self.bot.say('What roles should it add? (Must be comma separated)\nSay `None` to skip adding roles')

        answer = await self.bot.wait_for_message(timeout=120, author=author)
        if not answer:
            await self.bot.say("Timed out, canceling")
return

    @commands.command(no_pm=False, pass_context=True)
    async def beginadventure(self, ctx):
        """Begin your adventure."""

        await self.bot.say("You must make a choice. \nIn order to survive, you must kill person 1 or person 2")
        
        user = ctx.message.author.name
        answer = await self.bot.wait_for_message(timeout=10)
        
        if not answer:
            await self.bot.say("Time's up, " + user + " . Due to your indecisiveness, both Person 1 and Person 2 shall die.")
            return
        
        
def setup(bot):
    bot.add_cog(Adventure(bot)) 
