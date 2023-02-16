from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base
    DATABASE_URL: str
