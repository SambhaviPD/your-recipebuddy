from .common import get_recipe_using_openai

"""
Use GPT-4 to fetch recipes by meal course
"""


def invoke_recipes_by_mealcourse(settings, mealcourse, input_cuisine, number_of_recipes):

    api_key=settings.openai_api_key
    prompt = f"Write {number_of_recipes} Recipes where cuisine is {input_cuisine} \
        and the mealcourse is {mealcourse}. \
        Mention Cooking time and clear instructions on how to cook."
    success_message=f"Successfully returned {number_of_recipes} \
          for mealcourse {mealcourse} and cuisine {input_cuisine}"
    recipe = get_recipe_using_openai(api_key=api_key, \
                                    prompt=prompt, \
                                    success_message=success_message)
    return recipe