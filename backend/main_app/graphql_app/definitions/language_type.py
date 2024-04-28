import strawberry


@strawberry.type
class Language:
    id: strawberry.ID
    name: str
