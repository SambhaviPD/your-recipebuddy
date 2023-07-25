import requests

from .configuration import ResponseModel

"""
Use Spoonacular API to fetch one random recipe
"""
RANDOM_RECIPE_QUERY_KEYWORD = "/random"

def get_spoonacular_random_recipe(base_url, api_key):
    random_recipe_url = f"{base_url}{RANDOM_RECIPE_QUERY_KEYWORD}"
    headers = {"X-API-KEY": api_key}

    response = requests.get(random_recipe_url, headers=headers)
    response_data = {"response_data": response.json()}
    final_response = ResponseModel(
        success=True,
        message=f"Successfully returned a random recipe. Enjoy!",
        data=response_data,
    )
    return final_response


"""
Use GPT-4 API to fetch one random recipe
"""


def get_gpt4_random_recipe():
    final_response = ResponseModel(
        success=True, message=f"GPT-4 API is work in progress. Hang on!"
    )
    return final_response


def invoke_random_recipe(api_choice, settings):
    if api_choice.upper() == settings.default_backend.upper():
        recipe = get_spoonacular_random_recipe(
            base_url=settings.spoonacular_base_url, 
            api_key=settings.spoonacular_api_key
        )
    else:
        recipe = get_gpt4_random_recipe()

    return recipe
