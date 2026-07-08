import discord

from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, bot):

        self.bot = bot



    @discord.app_commands.command(
        name="test",
        description="Check if the bot works"
    )
    async def test(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.send_message(
            f"✅ Online in {interaction.guild.name}"
        )



async def setup(bot):

    await bot.add_cog(
        Test(bot)
    )