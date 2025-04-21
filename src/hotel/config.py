from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = True
    SECRET_KEY: str = "django-insecure-your-secret-key"
    ALLOWED_HOSTS: list[str] = ["*"]
    
    # Database settings
    DB_NAME: str = "hotel_db"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    # Additional settings
    DJANGO_SETTINGS_MODULE: str | None = None
    DATABASE_URL: str | None = None
    PYTHONPATH: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
