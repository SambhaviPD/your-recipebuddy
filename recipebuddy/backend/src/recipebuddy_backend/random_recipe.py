from .common import get_recipe_using_openai

"""
Use GPT-4 API to fetch one random recipe
"""

def invoke_random_recipe(settings):

    api_key=settings.openai_api_key
  
    prompt = f"""Your task is to generate a random recipe whose response is \
            in the form a table with 2 columns, where first column is one of: \
                Name:  \
                Cuisine:  \
                Cooking Time: \
                Ingredients: \
                Instructions: \
                    as Step 1:  and so on. \
                The second column should be the corresponding output. \
                Give the table a title "Here's a random recipe!" \
                
                Format everything as HTML that can be used in a website. \
                Place the description in a <div> element.
                \
                """
    success_message="Successfully returned a random recipe. Enjoy!"

    recipe = get_recipe_using_openai(api_key=api_key, \
                                     prompt=prompt, \
                                     success_message=success_message)
    return recipe

