from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = "Meditouch API"
    DB_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "changeme"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
