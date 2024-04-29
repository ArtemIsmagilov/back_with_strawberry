import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .database import Base


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    topics: Mapped[list["Topic"]] = relationship(back_populates="tag")


class Topic(Base):
    __tablename__ = "topic"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    tag_id: Mapped[int] = mapped_column(
        sa.ForeignKey("tag.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    tag: Mapped["Tag"] = relationship(back_populates="topics")
    materials: Mapped[list["Material"]] = relationship(back_populates="topic")
    pictures: Mapped[list["Picture"]] = relationship(back_populates="topic")
    videos: Mapped[list["Video"]] = relationship(back_populates="topic")


class Material(Base):
    __tablename__ = "material"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    topic_id: Mapped[int] = mapped_column(
        sa.ForeignKey("topic.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    topic: Mapped["Topic"] = relationship(back_populates="materials")
    sentences: Mapped[list["Sentence"]] = relationship(back_populates="material")


class Sentence(Base):
    __tablename__ = "sentence"

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str]
    material_id: Mapped[int] = mapped_column(
        sa.ForeignKey("material.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    language_id: Mapped[int] = mapped_column(
        sa.ForeignKey("language.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    material: Mapped["Material"] = relationship(back_populates="sentences")
    language: Mapped["Language"] = relationship(back_populates="sentences")
    voice: Mapped["Voice"] = relationship(back_populates="sentence")


class Language(Base):
    __tablename__ = "language"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    sentences: Mapped[list["Sentence"]] = relationship(back_populates="language")


class Voice(Base):
    __tablename__ = "voice"

    id: Mapped[int] = mapped_column(primary_key=True)
    voice_path: Mapped[str]
    sentence_id: Mapped[int] = mapped_column(
        sa.ForeignKey("sentence.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    sentence: Mapped["Sentence"] = relationship(back_populates="voice")


class Picture(Base):
    __tablename__ = "picture"

    id: Mapped[int] = mapped_column(primary_key=True)
    picture_path: Mapped[str]
    topic_id: Mapped[int] = mapped_column(
        sa.ForeignKey("topic.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    topic: Mapped["Topic"] = relationship(back_populates="pictures")


class Video(Base):
    __tablename__ = "video"

    id: Mapped[int] = mapped_column(primary_key=True)
    video_path: Mapped[str]
    topic_id: Mapped[int] = mapped_column(
        sa.ForeignKey("topic.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    topic: Mapped["Topic"] = relationship(back_populates="videos")
