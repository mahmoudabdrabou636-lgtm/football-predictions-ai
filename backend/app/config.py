from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Football Predictions AI"
    app_version: str = "0.1.0"
    environment: str = "development"

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int = 5432

    api_host: str = "0.0.0.0"
    api_port: int = 8000

    model_version: str = "0.1.0"
    model_path: str = "models/"

    log_level: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
