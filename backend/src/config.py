from functools import lru_cache

from pydantic import BaseSettings

class Settings(BaseSettings):
    # Until we provide the user an option to choose
    # between AI and non-AI, we default to Spoonacular
    default_backend: str = "Spoonacular"
    spoonacular_base_url: str 
    spoonacular_api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
