from .common import get_recipe_using_openai

"""
Use GPT-4 API to fetch one random recipe
"""

def invoke_random_recipe(settings):

    api_key=settings.openai_api_key
    recipe = """"
    "{ "Cuisine": "Mediterranean", "Cooking Time": "30 minutes", 
    "Ingredients": [ "2 boneless, skinless chicken breasts", 
    "1 tablespoon olive oil", "1 teaspoon dried oregano", 
    "1 teaspoon dried basil", "1/2 teaspoon garlic powder", 
    "1/2 teaspoon salt", "1/4 teaspoon black pepper", 
    "1 cup cherry tomatoes, halved", 
    "1/2 cup sliced black olives", 
    "1/4 cup crumbled feta cheese", 
    "2 tablespoons chopped fresh parsley" ], 
    "Instructions": [ "Step 1: Preheat the oven to 400°F (200°C).", 
    "Step 2: In a small bowl, mix together the dried oregano, dried basil, 
    garlic powder, salt, and black pepper.", 
    "Step 3: Place the chicken breasts on a baking sheet and drizzle with 
    olive oil. Sprinkle the spice mixture evenly over the chicken.", 
    "Step 4: Bake the chicken in the preheated oven for 20-25 minutes, 
    or until cooked through and no longer pink in the center.", 
    "Step 5: While the chicken is baking, prepare the tomato and olive topping.
    In a bowl, combine the cherry tomatoes, black olives, feta cheese, 
    and chopped parsley.", 
    "Step 6: Once the chicken is cooked, remove it from the oven 
    and let it rest for a few minutes. Then, top each chicken breast 
    with the tomato and olive mixture.", 
    "Step 7: Serve the chicken with a side of steamed vegetables or a 
    fresh salad. Enjoy!" ] }"
    """
    prompt = f"""Your task is to create a summary of the recipe generated by the AI. \
                Summarize the recipe below, delimited by triple backticks, in \
                atmost 50 words. \
                Recipe Summary: ```{recipe}```\
                """
    success_message="Successfully returned a random recipe. Enjoy!"

    recipe = get_recipe_using_openai(api_key=api_key, \
                                     prompt=prompt, \
                                     success_message=success_message)
    return recipe

