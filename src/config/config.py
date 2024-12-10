from pathlib import Path

import yaml
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class _SettingsModel(BaseSettings):
    """Базовые настройки."""

    @classmethod
    def from_yaml(cls, config_path: str) -> '_SettingsModel':
        return cls(
            **yaml.safe_load(Path(config_path).read_text(encoding='utf-8')),
        )

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix='EMP_',
        env_nested_delimiter='__',
    )

    @classmethod
    def customise_sources(
        cls,
        init_settings,
        env_settings,
        file_secret_settings,
    ):
        """Определяем приоритет использования переменных."""
        return init_settings, env_settings, file_secret_settings


class _ServiceSettings(_SettingsModel):
    """Валидация настроек из файла YAML."""

    title: str
    description: str
    host: str
    port: int
    debug: bool
    db_hostname: str
    db_port: int
    db_name: str
    db_collection_name: str
    tags_metadata: dict[str, str]


class _SettingsSecret(BaseSettings):
    """Валидация секретных данных."""

    MONGO_INITDB_ROOT_USERNAME: SecretStr = SecretStr('user')
    MONGO_INITDB_ROOT_PASSWORD: SecretStr = SecretStr('password')

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


class Settings(_SettingsModel, _SettingsSecret):
    """Настройки сервиса."""

    service: _ServiceSettings

    @property
    def database_url(self):
        """Ссылка для подключения к базе данных."""
        return (
            f'mongodb://'
            f'{self.MONGO_INITDB_ROOT_USERNAME.get_secret_value()}:'
            f'{self.MONGO_INITDB_ROOT_PASSWORD.get_secret_value()}@'
            f'{self.service.db_hostname}:{self.service.db_port}/'
        )


config = Settings.from_yaml('./src/config/config.yaml')
