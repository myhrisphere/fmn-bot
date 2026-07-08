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

        logger.info(
            "Database initialized"
        )


        # Load cogs
        await self.load_extension(
            "cogs.test"
        )

        logger.info(
            "Test cog loaded"
        )


        synced = await self.tree.sync()

        logger.info(
            f"Synced {len(synced)} commands"
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