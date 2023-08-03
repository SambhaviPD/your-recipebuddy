from .common import get_recipe_using_openai

"""
Use GPT-4 API to fetch one random recipe
"""

def invoke_random_recipe(settings):

    api_key=settings.openai_api_key
    prompt = "Write a Recipe with your own choice of Ingredients. \
        Mention Cooking time and clear instructions on how to cook \
        along with the cuisine of your recipe"
    success_message="Successfully returned a random recipe. Enjoy!"
    recipe = get_recipe_using_openai(api_key=api_key, \
                                       prompt=prompt, \
                                        success_message=success_message)
    return recipe

