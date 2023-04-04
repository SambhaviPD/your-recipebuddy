import requests

from enum import Enum
from functools import lru_cache

from fastapi import Depends, FastAPI, status, UploadFile
from typing_extensions import Annotated

from . import config

app = FastAPI(title="Recipe Buddy")

# Keywords that are used in the APIs
API_KEY_QUERY_KEYWORD = "?apiKey="
RECIPE_BY_CUISINE_QUERY_KEYWORD = "/complexSearch"

@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
async def home():
    return "Welcome to Recipe Buddy!"


@app.get("/recipes/surpriseme/")
async def get_recipes_random():
    pass

# Valid Cuisines that an end user is allowed to send
# If a cuisine  requested for is not in this list,
# we throw a 404 exception
class Cuisine(Enum):
    AFRICAN = "African"
    AMERICAN = "American"
    BRITISH = "British"
    CAJUN = "Cajun"
    CARIBBEAN = "Caribbean"
    CHINESE = "Chinese"
    EASTERN_EUROPEAN = "Eastern European"
    FRENCH = "French"
    GERMAN = "German"
    GREEK = "Greek"
    INDIAN = "Indian"
    IRISH = "Irish"
    ITALIAN = "Italian"
    JAPANESE = "Japanese"
    JEWISH = "Jewish"
    KOREAN = "Korean"
    LATIN_AMERICAN = "Latin American"
    MEDITERRANEAN = "Mediterranean"
    MEXICAN = "Mexican"
    MIDDLE_EASTERN = "Middle Eastern"
    NORDIC = "Nordic"
    SOUTHERN = "Southern"
    SPANISH = "Spanish"
    THAI = "Thai"
    VIETNAMESE = "Vietnamese"

"""
Use Spoonacular API to fetch recipes by cuisine
"""
def get_spoonacular_recipes_by_cuisine(settings, input_cuisine, number_of_recipes):
    recipes_by_cuisine_api = settings.spoonacular_base_url + RECIPE_BY_CUISINE_QUERY_KEYWORD \
        + API_KEY_QUERY_KEYWORD + settings.spoonacular_api_key + "&cuisine=" \
        + input_cuisine + "&number=" + str(number_of_recipes)
    response = requests.get(recipes_by_cuisine_api)
    return response.json()


def get_gpt4_recipes_by_cuisine():
    pass

"""
API to fetch recipes by cuisine
"""
@app.get("/recipes/cuisine")
async def get_recipes_by_cuisine(apiChoice: str, settings: Annotated[config.Settings, \
        Depends(get_settings)], input_cuisine: str, number_of_recipes: int = 1):
    cuisines = [cuisine.value for cuisine in Cuisine]
    if input_cuisine.capitalize() in cuisines:
        if settings.default_backend.upper() == apiChoice.upper():
            recipes = get_spoonacular_recipes_by_cuisine(settings, input_cuisine, \
                number_of_recipes)
            return recipes
        else:
            recipes = get_gpt4_recipes_by_cuisine()
    else:
        return status.HTTP_404_NOT_FOUND


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

