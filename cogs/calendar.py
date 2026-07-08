import discord

from discord.ext import commands

from discord import app_commands

from sqlalchemy import select


from database.database import AsyncSession

from database.models import Event


from ui.event_modal import EventModal



class Calendar(commands.Cog):


    def __init__(self, bot):

        self.bot = bot



    calendar = app_commands.Group(

        name="calendar",

        description="Event calendar"

    )



    # ==========================
    # ADD EVENT
    # ==========================

    @calendar.command(

        name="add",

        description="Create a new event"

    )
    async def add(

        self,

        interaction: discord.Interaction

    ):


        await interaction.response.send_modal(

            EventModal()

        )



    # ==========================
    # LIST EVENTS
    # ==========================

    @calendar.command(

        name="list",

        description="Show upcoming events"

    )
    async def list(

        self,

        interaction: discord.Interaction

    ):


        async with AsyncSession() as session:


            result = await session.execute(

                select(Event)

                .where(

                    Event.guild_id == interaction.guild.id

                )

                .where(

                    Event.archived == False

                )

                .order_by(

                    Event.start_datetime

                )

            )


            events = result.scalars().all()



        if not events:


            await interaction.response.send_message(

                "📅 No upcoming events.",

                ephemeral=True

            )

            return



        embed = discord.Embed(

            title="📅 Server Events",

            description=
            f"Showing {len(events)} events",

            color=discord.Color.blue()

        )



        for event in events:


            value = (

                f"🕒 **{event.start_datetime.strftime('%d.%m.%Y %H:%M')}**\n"

                f"👤 Created by <@{event.creator_id}>\n"

            )


            if event.category:

                value += (

                    f"🏷️ Category: `{event.category}`\n"

                )


            if event.description:

                value += (

                    f"📝 {event.description}"

                )



            embed.add_field(

                name=f"#{event.id} {event.title}",

                value=value,

                inline=False

            )



        await interaction.response.send_message(

            embed=embed

        )



async def setup(bot):

    await bot.add_cog(

        Calendar(bot)

    )