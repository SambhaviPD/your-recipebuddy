import requests

from enum import Enum

from .configuration import ResponseModel


RECIPE_BY_MEALCOURSE_QUERY_KEYWORD = "/complexSearch?&type="

class MealCourse(Enum):
    MAIN_COURSE = "main course"
    SIDE_DISH = "side dish"
    DESSERT = "dessert"
    APPETIZER = "appetizer"
    SALAD = "salad"
    BREAD = "bread"
    BREAKFAST = "breakfast"
    SOUP = "soup"
    BEVERAGE = "beverage"
    SAUCE = "sauce"
    MARINADE = "marinade"
    FINGERFOOD = "fingerfood"
    SNACK = "snack"
    DRINK = "drink"


"""
Use Spoonacular API to fetch recipes by meal course
"""


def get_spoonacular_recipes_by_mealcourse(
    base_url, api_key, mealcourse, number_of_recipes
):
    recipes_by_mealcourse_url = f"{base_url}{RECIPE_BY_MEALCOURSE_QUERY_KEYWORD}\
        {mealcourse}&number={str(number_of_recipes)}"
    headers = {"X-API-KEY": api_key}

    response = requests.get(recipes_by_mealcourse_url, headers=headers)
    response_data = {"response_data": response.json()}
    final_response = ResponseModel(
        success=True,
        message=f"Successfully returned {number_of_recipes} recipes that are {mealcourse}",
        data=response_data,
    )
    return final_response


"""
Use GPT-4 to fetch recipes by meal course
"""


def get_gpt4_recipes_by_mealcourse():
    pass


def invoke_recipes_by_mealcourse(
    api_choice, settings, mealcourse, number_of_recipes):

    if settings.default_backend.upper() == api_choice.upper():
        recipes = get_spoonacular_recipes_by_mealcourse(
            base_url=settings.spoonacular_base_url,
            api_key=settings.spoonacular_api_key,
            mealcourse=mealcourse,
            number_of_recipes=number_of_recipes,
        )
    else:
        recipes = get_gpt4_recipes_by_mealcourse()

    return recipes