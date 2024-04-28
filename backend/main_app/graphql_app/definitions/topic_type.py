import strawberry


@strawberry.type
class Topic:
    id: strawberry.ID
    title: str
    description: str
    tag_id: strawberry.ID
