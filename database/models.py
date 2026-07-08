from datetime import datetime

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)

from sqlalchemy import (
    Integer,
    String,
    Text,
    BigInteger,
    DateTime,
    Boolean
)

from config import DEFAULT_TIMEZONE


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
        default=DEFAULT_TIMEZONE
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )



# ==========================
# EVENTS
# ==========================

class Event(Base):

    __tablename__ = "events"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    # Server isolation
    guild_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True
    )


    # User who created the event
    creator_id: Mapped[int] = mapped_column(
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


    category: Mapped[str | None] = mapped_column(
        String,
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
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )



# ==========================
# AUDIT LOG
# ==========================

class AuditLog(Base):

    __tablename__ = "audit_logs"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    # Server isolation
    guild_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True
    )


    user_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True
    )


    action: Mapped[str] = mapped_column(
        String
    )


    target_type: Mapped[str] = mapped_column(
        String
    )


    target_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )


    description: Mapped[str] = mapped_column(
        Text
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )