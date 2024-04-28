from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncAttrs,
)
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3", echo=True)

async_session = async_sessionmaker(engine)
