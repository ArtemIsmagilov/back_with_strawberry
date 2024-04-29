import strawberry


@strawberry.type
class Language:
    id: strawberry.ID
    name: str


@strawberry.type
class Material:
    id: strawberry.ID
    name: str
    topic_id: strawberry.ID


@strawberry.type
class Picture:
    id: strawberry.ID
    picture_path: str
    topic_id: strawberry.ID


@strawberry.type
class Sentence:
    id: strawberry.ID
    body: str
    material_id: strawberry.ID
    language_id: strawberry.ID


@strawberry.type
class Tag:
    id: strawberry.ID
    name: str


@strawberry.type
class Topic:
    id: strawberry.ID
    title: str
    description: str
    tag_id: strawberry.ID


@strawberry.type
class Video:
    id: strawberry.ID
    video_path: str
    topic_id: strawberry.ID


@strawberry.type
class Voice:
    id: strawberry.ID
    voice_path: str
    sentence_id: strawberry.ID
