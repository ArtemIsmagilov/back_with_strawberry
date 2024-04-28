import strawberry


@strawberry.type
class Sentence:
    id: strawberry.ID
    body: str
    material_id: strawberry.ID
    language_id: strawberry.ID