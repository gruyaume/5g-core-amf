# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI = "sqlite:///./sql_app.db"


settings = Settings()
