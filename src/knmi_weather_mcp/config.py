from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the absolute path to the project root (two levels up from this file)
project_root = Path(__file__).parent.parent.parent
env_file_path = project_root / ".env"

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(env_file_path))
    knmi_api_key: str
    port: int = 8001


config = Config()
