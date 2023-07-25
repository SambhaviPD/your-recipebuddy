import requests

from .configuration import ResponseModel
from enum import Enum
from fastapi import status

"""
Use Spoonacular API to fetch recipes by ingredients
"""
RECIPE_BY_INGREDIENTS_QUERY_KEYWORD = "/findByIngredients"


# Valid Ingredients that an end user is allowed to send
# If an ingredient requested for is not in this list,
# we throw a 404 exception
# This is just a starter list, and not the final one
class Ingredient(Enum):
    BROCOLI = "Brocoli"
    CHEESE = "Cheese"
    MEAT = "Meat"
    MUSHROOM = "Mushroom"
    PASTA = "Pasta"
    TOMATO = "Tomato"


"""
Use Spoonacular API to fetch recipes by ingredients
"""


def get_spoonacular_recipes_by_ingredients(
    base_url, api_key, selected_ingredients, custom_ingredients, number_of_recipes
):
    recipes_by_ingredient_url = f"{base_url}{RECIPE_BY_INGREDIENTS_QUERY_KEYWORD}?&ingredients=\
        {selected_ingredients},{custom_ingredients}&number={str(number_of_recipes)}"
    headers = {"X-API-KEY": api_key}

    print("recipes_by_ingredient_url: ", recipes_by_ingredient_url)
    response = requests.get(recipes_by_ingredient_url, headers=headers)
    response_data = {"response_data": response.json()}
    final_response = ResponseModel(
        success=True,
        message=f"Successfully returned {number_of_recipes} recipe(s) that uses \
                    {selected_ingredients},{custom_ingredients}",
        data=response_data,
    )
    return final_response


"""
Use GPT-4 to fetch recipes by ingredients
"""


def get_gpt4_recipes_by_ingredients():
    pass


async def invoke_recipes_by_ingredients(
    api_choice, settings, selected_ingredients, \
    custom_ingredients, number_of_recipes,
):
    # Fetching enum values to a list
    ingredients = [ingredient.value for ingredient in Ingredient]
    # Split the string so that we will be able to compare individual ingredient
    selected_ingredients_list = [
        ingredient for ingredient in selected_ingredients.split(",")
    ]
    # Difference between input list and master list
    additional_ingredients = set(selected_ingredients_list).difference(set(ingredients))
    # If we do not have any additional ingredients, we proceed
    if not additional_ingredients:
        if settings.default_backend.upper() == api_choice.upper():
            recipes = get_spoonacular_recipes_by_ingredients(
                base_url=settings.spoonacular_base_url,
                api_key=settings.spoonacular_api_key,
                selected_ingredients=selected_ingredients,
                custom_ingredients=custom_ingredients,
                number_of_recipes=number_of_recipes,
            )
            return recipes
        else:
            recipes = get_gpt4_recipes_by_ingredients()
    # Throw an error if any additional ingredient is present as part os user input
    else:
        error_response = ResponseModel(
            success=False,
            message=f"Sorry, {additional_ingredients} are not present in our master list. ",
            data={"error_code": status.HTTP_404_NOT_FOUND},
        )
        return error_response