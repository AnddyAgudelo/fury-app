from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION: str
    DB_NAME: str
    API_STR: str = "/api"


settings = Settings()
