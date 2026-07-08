import asyncio

import logging


import discord

from discord.ext import commands


from config import (
    DISCORD_TOKEN,
    LOG_LEVEL
)


from database.database import (
    init_database
)



logging.basicConfig(

    level=getattr(
        logging,
        LOG_LEVEL.upper(),
        logging.INFO
    ),

    format=
    "[%(asctime)s] %(levelname)s: %(message)s"

)



class FMNBot(commands.Bot):


    def __init__(self):

        intents = discord.Intents.default()


        super().__init__(

            command_prefix="!",

            intents=intents

        )



    async def setup_hook(self):

        logging.info(
            "Initializing database..."
        )


        await init_database()


        logging.info(
            "Database initialized"
        )


        await self.load_extension(
            "cogs.calendar"
        )


        logging.info(
            "Calendar cog loaded"
        )


        await self.tree.sync()


        logging.info(
            "Commands synchronized"
        )



bot = FMNBot()



async def main():

    async with bot:

        await bot.start(
            DISCORD_TOKEN
        )



asyncio.run(main())