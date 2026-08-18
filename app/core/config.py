from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    '''
    Defines the central configuration used by the workflow engine.

    Default values can be overridden through environment variables or values loaded from the .env file.
    '''

    app_name: str = "AI Workflow Engine"
    environment: str = "development"
    log_level: str = "INFO"
    max_tasks: int = 10
    tool_timeout: float = 10.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
        )

settings = Settings()
