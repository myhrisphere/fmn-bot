from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)


from database.models import Base


from config import DATABASE_URL



engine = create_async_engine(

    DATABASE_URL,

    echo=False

)



AsyncSession = async_sessionmaker(

    engine,

    expire_on_commit=False

)



async def init_database():

    async with engine.begin() as conn:

        await conn.run_sync(

            Base.metadata.create_all

        )