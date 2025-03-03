import logging
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent.parent

class LoggingConfig(BaseModel):
    level: Literal[
        'debug',
        'info',
        'warning',
        'error',
        'critical',
    ] = 'info'
    format: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
    date_format: str = "%Y-%m-%d %H:%M:%S"
    
    @property
    def level_value(self) -> int:
        return logging.getLevelNamesMapping()[self.level.upper()]

class APIKeysConfig(BaseModel):
    openweathermap: str

class PostgresConfig(BaseModel):
    url: PostgresDsn
    sync_url: PostgresDsn
    user: str
    password: str
    host: str
    name: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    
    @property
    def migrations_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.name}"    

class Settings(BaseSettings):
    logging: LoggingConfig
    api_keys: APIKeysConfig
    database: PostgresConfig
    

    class Config:
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


settings = Settings()