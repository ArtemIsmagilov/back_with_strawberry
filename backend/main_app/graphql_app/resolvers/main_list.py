from ..usecases.tag_topic_usecase import TagTopic
from ...sql_app import crud
from ...sql_app.database import async_session


async def get_main_list() -> list["TagTopic"]:
    async with async_session() as session:
        topics_tags = await crud.read_topics_tags(session)

    result = [
        TagTopic(
            topic_id=row.id,
            topic_title=row.title,
            topic_description=row.description,
            tag_id=row.tag_id,
            tag_name=row.name,
        )
        for row in topics_tags
    ]
    return result
