from datetime import datetime

from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)



class Base(DeclarativeBase):
    pass



class GuildSettings(Base):

    __tablename__ = "guild_settings"


    guild_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )


    timezone: Mapped[str] = mapped_column(
        String,
        default="UTC"
    )


    reminder_mode: Mapped[str] = mapped_column(
        String,
        default="DM"
    )


    reminder_channel: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True
    )


    birthday_channel: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    from datetime import datetime

from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    Text,
    Integer
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)


class Base(DeclarativeBase):
    pass


# ==========================
# SERVER SETTINGS
# ==========================

class GuildSettings(Base):

    __tablename__ = "guild_settings"


    guild_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )


    timezone: Mapped[str] = mapped_column(
        String,
        default="UTC"
    )


    reminder_mode: Mapped[str] = mapped_column(
        String,
        default="DM"
    )


    reminder_channel: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True
    )


    birthday_channel: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )



# ==========================
# CATEGORIES
# ==========================

class Category(Base):

    __tablename__ = "categories"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    guild_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True
    )


    name: Mapped[str] = mapped_column(
        String
    )


    color: Mapped[str] = mapped_column(
        String,
        default="#5865F2"
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )



# ==========================
# APPOINTMENTS
# ==========================

class Appointment(Base):

    __tablename__ = "appointments"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    # IMPORTANT:
    # Every query will use this.
    guild_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True
    )


    title: Mapped[str] = mapped_column(
        String
    )


    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )


    start_datetime: Mapped[datetime] = mapped_column(
        DateTime
    )


    end_datetime: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )


    category_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "categories.id"
        ),
        nullable=True
    )


    creator_id: Mapped[int] = mapped_column(
        BigInteger
    )


    last_editor_id: Mapped[int | None] = mapped_column(
        BigInteger,
        nullable=True
    )


    archived: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )



# ==========================
# PARTICIPANTS
# ==========================

class AppointmentParticipant(Base):

    __tablename__ = "appointment_participants"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    appointment_id: Mapped[int] = mapped_column(
        ForeignKey(
            "appointments.id"
        )
    )


    user_id: Mapped[int] = mapped_column(
        BigInteger
    )



# ==========================
# REMINDERS
# ==========================

class Reminder(Base):

    __tablename__ = "reminders"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    appointment_id: Mapped[int] = mapped_column(
        ForeignKey(
            "appointments.id"
        )
    )


    minutes_before: Mapped[int]


    sent: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )



# ==========================
# RECURRING EVENTS
# ==========================

class Recurrence(Base):

    __tablename__ = "recurrences"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    appointment_id: Mapped[int] = mapped_column(
        ForeignKey(
            "appointments.id"
        )
    )


    type: Mapped[str] = mapped_column(
        String
    )


    interval: Mapped[int] = mapped_column(
        Integer,
        default=1
    )


    until: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )



# ==========================
# EDIT HISTORY
# ==========================

class AppointmentHistory(Base):

    __tablename__ = "appointment_history"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    appointment_id: Mapped[int]


    editor_id: Mapped[int]


    field_changed: Mapped[str]


    old_value: Mapped[str | None]


    new_value: Mapped[str | None]


    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )