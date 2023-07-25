import requests

from enum import Enum
from fastapi import status

from .configuration import ResponseModel


"""
Use Spoonacular API to fetch recipes by cuisine
"""
RECIPE_BY_CUISINE_QUERY_KEYWORD = "/complexSearch"


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


def get_spoonacular_recipes_by_cuisine(
    base_url, api_key, input_cuisine, number_of_recipes
):
    recipes_by_cuisine_url = f"{base_url}{RECIPE_BY_CUISINE_QUERY_KEYWORD}?&cuisine=\
        {input_cuisine}&number={str(number_of_recipes)}"
    headers = {"X-API-KEY": api_key}

    response = requests.get(recipes_by_cuisine_url, headers=headers)
    response_data = {"response_data": response.json()}
    final_response = ResponseModel(
        success=True,
        message=f"Successfully returned {number_of_recipes} {input_cuisine.capitalize()} cuisine recipes",
        data=response_data,
    )
    return final_response


""""
Use GPT-4 to fetch recipes by cuisine
"""


def get_gpt4_recipes_by_cuisine():
    pass


"""
API to fetch recipes by cuisine
"""


def invoke_recipes_by_cuisine(api_choice, settings, input_cuisine, number_of_recipes):
    # Fetching enum values to a list
    cuisines = [cuisine.value for cuisine in Cuisine]
    # Check if cuisine input is present in the list
    if input_cuisine.capitalize() in cuisines:
        if settings.default_backend.upper() == api_choice.upper():
            recipes = get_spoonacular_recipes_by_cuisine(
                base_url=settings.spoonacular_base_url,
                api_key=settings.spoonacular_api_key,
                input_cuisine=input_cuisine,
                number_of_recipes=number_of_recipes,
            )
            return recipes
        else:
            recipes = get_gpt4_recipes_by_cuisine()
    # Throw an error since cuisine input is not present in the list
    else:
        error_response = ResponseModel(
            success=False,
            message=f"Sorry, no recipes of {input_cuisine} were found",
            data={"error_code": status.HTTP_404_NOT_FOUND},
        )
        return error_response
