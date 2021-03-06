from discord.ext import commands
import discord


class EmbedHelpCommand(commands.HelpCommand):
    """This is an example of a HelpCommand that utilizes embeds.
    It's pretty basic but it lacks some nuances that people might expect.
    1. It breaks if you have more than 25 cogs or more than 25 subcommands. (Most people don't reach this)
    2. It doesn't DM users. To do this, you have to override `get_destination`. It's simple.
    Other than those two things this is a basic skeleton to get you started. It should
    be simple to modify if you desire some other behaviour.

    To use this, pass it to the bot constructor e.g.:

    bot = commands.Bot(help_command=EmbedHelpCommand())
    """

    def get_command_signature(self, command):
        return '{0.qualified_name} {0.signature}'.format(command)

    async def send_bot_help(self, mapping):
        COLOUR = discord.Colour.dark_green
        embed = discord.Embed(title='Grick Heart Commands', colour=0x239B56)
        embed.add_field(name='Roll Command', value='You can roll any dice on the planet with `!roll <dice number>` (replace <dice number> with the number of dice you want e.i. for d20 you would do `!roll 20`.', inline=True)
        embed.add_field(name='Spell Command', value='You can look up any spell in the D&D universe with `!spell <spell name>`. Currently, please use no spaces in the spellname (will be changed in the future).', inline=True)
        embed.add_field(name='Game Command', value='This command allows DMs to control who is in the game. You can add players with `!game add <player>` and remove them with `!game remove <player>`. Be sure that you have set up your roles and channels correctly!', inline=True)
        embed.add_field(name='Initiative Command', value="By far the most handy command in the bot, you can roll for initiative with `!init roll <modifiers>` and then see your initiative number with `!init whatsmy`. You can also see all member's number with `!init list`.", inline=True)
        await self.get_destination().send(embed=embed)