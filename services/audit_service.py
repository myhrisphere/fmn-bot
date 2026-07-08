from database.database import AsyncSession
from database.models import AuditLog



async def create_audit_log(
    guild_id: int,
    user_id: int,
    action: str,
    target_type: str,
    description: str,
    target_id: int | None = None
):

    log = AuditLog(

        guild_id=guild_id,

        user_id=user_id,

        action=action,

        target_type=target_type,

        target_id=target_id,

        description=description

    )


    async with AsyncSession() as session:

        session.add(log)

        await session.commit()