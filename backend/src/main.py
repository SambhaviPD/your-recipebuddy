import requests

from enum import Enum
from functools import lru_cache

from fastapi import Depends, FastAPI, status, UploadFile

from typing_extensions import Annotated

from pydantic import BaseModel

import config


app = FastAPI(title="Recipe Buddy")

# Keywords that are used in the APIs
API_KEY_QUERY_KEYWORD = "?apiKey="
RANDOM_RECIPE_QUERY_KEYWORD = "/random"
RECIPE_BY_CUISINE_QUERY_KEYWORD = "/complexSearch"


@lru_cache()
def get_settings():
    return config.Settings()


"""
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
def get_spoonacular_recipes_by_cuisine(base_url, api_key, input_cuisine, number_of_recipes):
    recipes_by_cuisine_url = f"{base_url}{RECIPE_BY_CUISINE_QUERY_KEYWORD}?&cuisine=\
        {input_cuisine}&number={str(number_of_recipes)}"
    headers = {"X-API-KEY" : api_key}

    response = requests.get(recipes_by_cuisine_url, headers=headers)
    response_data = {
        "response_data" : response.json()
    }
    final_response = ResponseModel(success=True, \
                    message=f"Successfully returned recipes by {input_cuisine.capitalize()} Cuisine", \
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


def get_gpt4_recipes_by_cuisine():
    pass

"""
API to fetch recipes by cuisine
"""
@app.get("/recipes/cuisine", status_code=200, response_model=ResponseModel)
async def get_recipes_by_cuisine(api_choice: str, settings: Annotated[config.Settings, \
        Depends(get_settings)], input_cuisine: str, number_of_recipes: int = 1):
    
    # Fetching enum values to a list
    cuisines = [cuisine.value for cuisine in Cuisine]
    # Check if cuisine input is present in the list
    if input_cuisine.capitalize() in cuisines:
        if settings.default_backend.upper() == api_choice.upper():
            recipes = get_spoonacular_recipes_by_cuisine(base_url=settings.spoonacular_base_url, \
                        api_key=settings.spoonacular_api_key, \
                        input_cuisine=input_cuisine, number_of_recipes=number_of_recipes)
            return recipes
        else:
            recipes = get_gpt4_recipes_by_cuisine()
    # Throw an error since cuisine input is not present in the list
    else:
        error_response = ResponseModel(success=False, \
                    message=f"Sorry, no recipes of {input_cuisine} were found",
                    data={
                        "error_code" : status.HTTP_404_NOT_FOUND
                        })
        return error_response


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

