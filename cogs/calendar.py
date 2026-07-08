from datetime import datetime

import discord

from discord.ext import commands

from discord import app_commands

from sqlalchemy import select, delete

from database.database import AsyncSession

from database.models import Appointment



class Calendar(commands.Cog):

    def __init__(self, bot):

        self.bot = bot



    calendar = app_commands.Group(
        name="calendar",
        description="Calendar commands"
    )


    # =========================
    # ADD APPOINTMENT
    # =========================

    @calendar.command(
        name="add",
        description="Add a new appointment"
    )
    async def add(
        self,
        interaction: discord.Interaction,
        title: str,
        date: str,
        time: str,
        description: str = None
    ):


        try:

            start = datetime.strptime(
                f"{date} {time}",
                "%d.%m.%Y %H:%M"
            )

        except ValueError:

            await interaction.response.send_message(
                "Wrong date format. Use DD.MM.YYYY HH:MM",
                ephemeral=True
            )

            return



        appointment = Appointment(

            guild_id=interaction.guild.id,

            title=title,

            description=description,

            start_datetime=start,

            creator_id=interaction.user.id

        )


        async with AsyncSession() as session:

            session.add(
                appointment
            )

            await session.commit()



        await interaction.response.send_message(
            f"Appointment created:\n"
            f"**{title}**\n"
            f"{start.strftime('%d.%m.%Y %H:%M')}"
        )



    # =========================
    # LIST APPOINTMENTS
    # =========================

    @calendar.command(
        name="list",
        description="Show upcoming appointments"
    )
    async def list(
        self,
        interaction: discord.Interaction
    ):


        async with AsyncSession() as session:


            result = await session.execute(

                select(Appointment)
                .where(
                    Appointment.guild_id
                    ==
                    interaction.guild.id
                )
                .where(
                    Appointment.is_archived
                    ==
                    False
                )

            )


            appointments = result.scalars().all()



        if not appointments:

            await interaction.response.send_message(
                "No appointments found."
            )

            return



        embed = discord.Embed(
            title="📅 Calendar",
            color=discord.Color.blue()
        )


        for appointment in appointments:


            embed.add_field(

                name=appointment.title,

                value=
                f"{appointment.start_datetime.strftime('%d.%m.%Y %H:%M')}\n"
                f"Created by <@{appointment.creator_id}>",

                inline=False

            )



        await interaction.response.send_message(
            embed=embed
        )



    # =========================
    # DELETE APPOINTMENT
    # =========================

    @calendar.command(
        name="delete",
        description="Delete an appointment"
    )
    async def delete(
        self,
        interaction: discord.Interaction,
        appointment_id: int
    ):


        async with AsyncSession() as session:


            result = await session.execute(

                select(Appointment)
                .where(
                    Appointment.id
                    ==
                    appointment_id
                )
                .where(
                    Appointment.guild_id
                    ==
                    interaction.guild.id
                )

            )


            appointment = result.scalar_one_or_none()



            if not appointment:

                await interaction.response.send_message(
                    "Appointment not found.",
                    ephemeral=True
                )

                return



            await session.delete(
                appointment
            )

            await session.commit()



        await interaction.response.send_message(
            "Appointment deleted."
        )



async def setup(bot):

    await bot.add_cog(
        Calendar(bot)
    )