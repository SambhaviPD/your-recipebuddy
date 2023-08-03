"""
Use GPT-4 to fetch recipes by ingredients
"""


def get_gpt4_recipes_by_ingredients():
    pass


async def invoke_recipes_by_ingredients(
    api_choice, settings, selected_ingredients, \
    custom_ingredients, number_of_recipes,
):
    recipes = get_gpt4_recipes_by_ingredients()
    return recipes