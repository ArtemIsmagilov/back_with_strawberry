from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Topic, Tag


async def read_topics_tags(session: AsyncSession):
    stmt = (
        select(Topic.id, Topic.title, Topic.description, Topic.tag_id, Tag.name)
        .join(Tag, Topic.tag_id == Tag.id)
        .order_by(Topic.id)
    )
    return await session.execute(stmt)
