from datetime import datetime


import discord


from database.database import AsyncSession

from database.models import Event


from services.audit_service import create_audit_log



class EventModal(
    discord.ui.Modal,
    title="Create Event"
):


    title_input = discord.ui.TextInput(

        label="Event name",

        placeholder="Example: Gaming night"

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

        required=False,

        style=discord.TextStyle.paragraph

    )


    category_input = discord.ui.TextInput(

        label="Category",

        placeholder="Work / Personal / Gaming / School",

        required=False

    )



    async def on_submit(
        self,
        interaction: discord.Interaction
    ):


        try:

            start = datetime.strptime(

                f"{self.date_input.value} {self.time_input.value}",

                "%d.%m.%Y %H:%M"

            )


        except ValueError:


            await interaction.response.send_message(

                "❌ Invalid date format. Use DD.MM.YYYY HH:MM",

                ephemeral=True

            )

            return



        event = Event(

            guild_id=interaction.guild.id,

            creator_id=interaction.user.id,

            title=self.title_input.value,

            description=self.description_input.value,

            category=self.category_input.value,

            start_datetime=start

        )


        async with AsyncSession() as session:

            session.add(event)

            await session.commit()

            await session.refresh(event)



        await create_audit_log(

            guild_id=interaction.guild.id,

            user_id=interaction.user.id,

            action="CREATE",

            target_type="EVENT",

            target_id=event.id,

            description=f"Created event: {event.title}"

        )



        await interaction.response.send_message(

            f"✅ Event created:\n"
            f"**{event.title}**\n"
            f"📅 {start.strftime('%d.%m.%Y %H:%M')}",

            ephemeral=True

        )