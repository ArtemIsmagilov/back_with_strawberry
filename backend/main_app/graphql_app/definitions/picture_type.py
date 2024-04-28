import strawberry


@strawberry.type
class Picture:
    id: strawberry.ID
    picture_path: str
    topic_id: strawberry.ID
