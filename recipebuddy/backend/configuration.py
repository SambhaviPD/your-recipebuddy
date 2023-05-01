from pydantic import BaseSettings
import pathlib

cfd = pathlib.Path(__file__).parent.absolute()
env_path = cfd / ".env"

class Settings(BaseSettings):
    # Until we provide the user an option to choose
    # between AI and non-AI, we default to Spoonacular
    default_backend: str = "Spoonacular"

    spoonacular_base_url: str 
    spoonacular_api_key: str

    class Config:
        env_file = env_path
        env_file_encoding = "utf-8"

