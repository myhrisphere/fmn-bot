import discord

from datetime import datetime

from database.database import AsyncSession
from database.models import Appointment



class AppointmentModal(
    discord.ui.Modal,
    title="Create Appointment"
):


    title_input = discord.ui.TextInput(
        label="Title",
        placeholder="Example: Dentist"
    )


    date_input = discord.ui.TextInput(
        label="Date",
        placeholder="DD.MM.YYYY"
    )


    time_input = discord.ui.TextInput(
        label="Time",
        placeholder="HH:MM"
    )


    description_input = discord.ui.TextInput(
        label="Description",
        required=False
    )


    async def on_submit(
        self,
        interaction: discord.Interaction
    ):


        try:

            date = datetime.strptime(
                f"{self.date_input.value} {self.time_input.value}",
                "%d.%m.%Y %H:%M"
            )


        except ValueError:

            await interaction.response.send_message(
                "Invalid date format.",
                ephemeral=True
            )

            return



        appointment = Appointment(

            guild_id=interaction.guild.id,

            title=self.title_input.value,

            description=self.description_input.value,

            start_datetime=date,

            creator_id=interaction.user.id

        )


        async with AsyncSession() as session:

            session.add(
                appointment
            )

            await session.commit()



        await interaction.response.send_message(
            f"Created:\n"
            f"**{appointment.title}**\n"
            f"{date.strftime('%d.%m.%Y %H:%M')}"
        )