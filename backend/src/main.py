import requests

from enum import Enum
from functools import lru_cache

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

from pydantic import BaseModel

import config

app = FastAPI(title="Recipe Buddy")

# Keywords that are used in the APIs
API_KEY_QUERY_KEYWORD = "?apiKey="
RANDOM_RECIPE_QUERY_KEYWORD = "/random"


@lru_cache()
def get_settings():
    return config.Settings()


""""
Class that corresponds to requests.model.Response
Adding only 3 fields now. As need arises we can add
more like content, headers, etc.,
"""
class ResponseModel(BaseModel):
    success: bool
    message: str
    data: dict
    

@app.get("/")
async def home():
    return "Welcome to Recipe Buddy!"

"""
Use Spoonacular API to fetch one random recipe
"""
def get_spoonacular_random_recipe(base_url, api_key):
    random_recipe_url = f"{base_url}{RANDOM_RECIPE_QUERY_KEYWORD}"
    headers = {"X-API-KEY" : api_key}
    
    response = requests.get(random_recipe_url, headers=headers)
    response_data = {
        "response_data" : response.json()
    }
    final_response = ResponseModel(success=True, \
                        message=f"Successfully returned a random recipe. Enjoy!", \
                        data=response_data)
    
    return final_response


"""
Use GPT-4 API to fetch one random recipe
"""
def get_gpt4_random_recipe():
    pass

@app.get("/recipes/random", status_code=200, response_model=ResponseModel)
async def get_recipes_random(api_choice: str, settings: Annotated[config.Settings, \
    Depends(get_settings)]):
    if settings.default_backend.upper() == api_choice.upper():
        recipe = get_spoonacular_random_recipe(base_url=settings.spoonacular_base_url, \
                                    api_key=settings.spoonacular_api_key)
    else:
        get_gpt4_random_recipe()

    return recipe


class Cuisine(str, Enum):
    chinese = "chinese"
    continental = "continental"
    indian = "indian"
    sushi = "sushi"
    thai = "thai"


@app.get("/recipes/{cuisine}")
async def get_recipes_by_cuisine(cuisine: str):
    return {"message" : "Here you go..."}


# @app.get("/recipes/{ingredients}")
# async def get_recipes_by_ingredients(ingredients: list[str]):
#     pass


@app.get("/recipes/{mealcourse}")
async def get_recipes_by_mealcourse(mealcourse: str):
    return {"message" : "Here are some recipes by meal course!"}


# @app.get("/recipes/{image}")
# async def get_recipes_by_image(image: UploadFile):
#     pass


# @app.get("/recipes/{images}")
# async def get_recipe_by_images(images: UploadFile):
#     pass

