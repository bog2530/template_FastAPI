import os
from logging import config as logging_config

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

from core.logging import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Название проекта. Используется в Swagger-документации
    PROJECT_NAME: str = 'movies'

    # Настройки Redis
    REDIS_HOST: str = Field(alias='REDIS_CACHE_HOST')
    REDIS_PORT: int = Field(alias='REDIS_CACHE_PORT')

    # Настройки Elasticsearch
    ELASTIC_SCHEMA: str
    ELASTIC_HOST: str
    ELASTIC_PORT: int

    # Корень проекта
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


settings = Settings()