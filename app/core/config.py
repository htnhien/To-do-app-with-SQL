import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "To-do List API"
    DATABASE_URL: str = "sqlite:///./test.db"

settings = Settings()