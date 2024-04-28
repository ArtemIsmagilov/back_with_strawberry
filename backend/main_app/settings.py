import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_ECHO = os.environ["SQLALCHEMY_ECHO"]
    SQLALCHEMY_URL = os.environ["SQLALCHEMY_URL"]
    ...


class TestConfig:
    ...
