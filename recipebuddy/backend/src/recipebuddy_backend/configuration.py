from functools import lru_cache
from pydantic import BaseModel, BaseSettings
from typing import Optional

import pathlib

cfd = pathlib.Path(__file__).parent.parent.absolute()
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

@lru_cache()
def get_settings():
    return Settings()


"""
Class that corresponds to requests.model.Response
Adding only 3 fields now. As need arises we can add
more like content, headers, etc.,
"""


class ResponseModel(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None