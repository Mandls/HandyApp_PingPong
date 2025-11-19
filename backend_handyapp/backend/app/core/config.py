import warnings
import secrets
from typing import Literal
 
from pydantic import (
    AnyUrl,
    computed_field,
    model_validator,
)
from typing_extensions import Self
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
 
 
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_ignore_empty=True,
        extra="ignore",
    )
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
 
    PROJECT_NAME: str = "Handyapp_PingPong"
    SQL_SERVER: str = "192.168.19.62"
    SQL_PORT: int = 0
    SQL_USER: str = "sa"
    SQL_PASSWORD: str = "changethis"
    SQL_DB: str = "handyapp"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> AnyUrl:
        base = MultiHostUrl.build(
            scheme="mssql+pyodbc",
            username=self.SQL_USER,
            password=self.SQL_PASSWORD,
            host=self.SQL_SERVER,
            port=self.SQL_PORT,
            path=self.SQL_DB
        )
        return f"{base}?driver=ODBC+Driver+17+for+SQL+Server"
   
   
    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        if value == "changethis":
            message = (
                f'The value of {var_name} is "...", '
                "for security, please change it, at least for deployments."
            )
            if self.ENVIRONMENT == "local":
                warnings.warn(message, stacklevel=1)
            else:
                raise ValueError(message)
 
    @model_validator(mode="after")
    def _enforce_non_default_secrets(self) -> Self:
        self._check_default_secret("SQL_PASSWORD", self.SQL_PASSWORD)
        return self
   
settings = Settings()