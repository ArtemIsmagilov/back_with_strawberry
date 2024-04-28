import strawberry


@strawberry.type
class Video:
    id: strawberry.ID
    video_path: str
    topic_id: strawberry.ID
