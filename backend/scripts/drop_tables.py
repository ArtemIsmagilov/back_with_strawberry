import asyncio


async def main():
    from backend.main_app.sql_app.database import engine
    from backend.main_app.sql_app.models import Base

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


if __name__ == "__main__":
    asyncio.run(main())
