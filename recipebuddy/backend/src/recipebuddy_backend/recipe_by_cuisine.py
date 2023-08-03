from .common import get_recipe_using_openai

""""
Use GPT-4 to fetch recipes by cuisine
"""

def invoke_recipes_by_cuisine(settings, input_cuisine, number_of_recipes):
    api_key=settings.openai_api_key
    prompt = f"Write {number_of_recipes} Recipes where cuisine is {input_cuisine}. \
        Use commonly used Ingredients in {input_cuisine}. \
        Mention Cooking time and clear instructions on how to cook"
    success_message=f"Successfully returned {number_of_recipes} \
          {input_cuisine} cuisine recipes"
    recipe = get_recipe_using_openai(api_key=api_key, \
                                    prompt=prompt, \
                                    success_message=success_message)
    return recipe