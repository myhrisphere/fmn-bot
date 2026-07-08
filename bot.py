import discord

from discord.ext import commands

from config import DISCORD_TOKEN

from database.database import create_database

from utils.logger import (
    setup_logger,
    logger
)


class CalendarBot(commands.Bot):

    async def setup_hook(self):

        await create_database()

        extensions = [
            "cogs.test",
            "cogs.calendar",
        ]


        for extension in extensions:

            await self.load_extension(
                extension
            )


        await self.tree.sync()


        logger.info(
            "Commands synchronized"
        )



intents = discord.Intents.default()

intents.members = True


bot = CalendarBot(
    command_prefix="!",
    intents=intents
)



@bot.event
async def on_ready():

    logger.info(
        f"Logged in as {bot.user}"
    )



async def main():

    setup_logger()

    await bot.start(
        DISCORD_TOKEN
    )



if __name__ == "__main__":

    import asyncio

    asyncio.run(main())