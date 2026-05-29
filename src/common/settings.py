from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Capstone Multi-Agent AI Platform"
    app_env: str = "local"
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db: str = "capstone_db"
    use_azure_openai: bool = False
    azure_openai_endpoint: str | None = None
    azure_openai_api_key: str | None = None
    azure_openai_deployment: str = "gpt-4.1"
    azure_openai_api_version: str = "2025-01-01-preview"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
