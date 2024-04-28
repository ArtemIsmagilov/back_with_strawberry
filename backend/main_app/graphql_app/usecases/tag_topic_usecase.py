import strawberry


@strawberry.type
class TagTopic:
    topic_id: strawberry.ID
    topic_title: str
    topic_description: str
    tag_id: strawberry.ID
    tag_name: str
