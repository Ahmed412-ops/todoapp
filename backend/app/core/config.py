import os

from pydantic_settings import BaseSettings


ENV_FILE = os.getenv(
    "ENV_FILE",
    ".env.dev"
)


class Settings(BaseSettings):

    DATABASE_URL: str

    class Config:
        env_file = ENV_FILE


settings = Settings()