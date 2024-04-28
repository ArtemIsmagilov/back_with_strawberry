import strawberry


@strawberry.type
class Material:
    id: strawberry.ID
    name: str
    topic_id: strawberry.ID
