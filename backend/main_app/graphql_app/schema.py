import strawberry

from .usecases.tag_topic_usecase import TagTopic
from .resolvers.main_list import get_main_list


@strawberry.type
class Query:
    get_main_list: list["TagTopic"] = strawberry.field(resolver=get_main_list)


schema = strawberry.Schema(query=Query)
