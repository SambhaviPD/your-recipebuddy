import requests

from enum import Enum
from functools import lru_cache

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

from . import config

app = FastAPI(title="Recipe Buddy")

# Keywords that are used in the APIs
API_KEY_QUERY_KEYWORD = "?apiKey="
RANDOM_RECIPE_QUERY_KEYWORD = "/random"


@lru_cache()
def get_settings():
    return config.Settings()

@app.get("/")
async def home():
    return "Welcome to Recipe Buddy!"

"""
Use Spoonacular API to fetch one random recipe
"""
def get_spoonacular_random_recipe(settings):
    random_recipe_api = settings.spoonacular_base_url + RANDOM_RECIPE_QUERY_KEYWORD \
        + API_KEY_QUERY_KEYWORD + settings.spoonacular_api_key
    response = requests.get(random_recipe_api)
    return response.json()


"""
Use GPT-4 API to fetch one random recipe
"""
def get_gpt4_random_recipe():
    pass

@app.get("/recipes/random")
async def get_recipes_random(apiChoice: str, settings: Annotated[config.Settings, \
    Depends(get_settings)]):
    if settings.default_backend.upper() == apiChoice.upper():
        recipe = get_spoonacular_random_recipe(settings)
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
async def get_recipes_by_cuisine(cuisine: Cuisine):
    pass


# @app.get("/recipes/{ingredients}")
# async def get_recipes_by_ingredients(ingredients: list[str]):
#     pass


@app.get("/recipes/{mealcourse}")
async def get_recipes_by_mealcourse(mealcourse: str):
    pass


# @app.get("/recipes/{image}")
# async def get_recipes_by_image(image: UploadFile):
#     pass


# @app.get("/recipes/{images}")
# async def get_recipe_by_images(images: UploadFile):
#     pass

