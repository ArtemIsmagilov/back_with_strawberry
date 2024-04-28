import strawberry


@strawberry.type
class Voice:
    id: strawberry.ID
    voice_path: str
    sentence_id: strawberry.ID
