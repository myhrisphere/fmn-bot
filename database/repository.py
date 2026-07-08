from database.database import AsyncSession


async def get_session():

    async with AsyncSession() as session:
        yield session