from fastapi import Depends, FastAPI, Query

from typing_extensions import Annotated

from .configuration import Settings, ResponseModel, get_settings
from .random_recipe import invoke_random_recipe
from .recipe_by_cuisine import invoke_recipes_by_cuisine
from .recipe_by_ingredients import invoke_recipes_by_ingredients
from .recipe_by_mealcourse import invoke_recipes_by_mealcourse

app = FastAPI(title="Recipe Buddy")


@app.get("/")
async def home():
    return "Welcome to Recipe Buddy!"


@app.get("/recipes/random", status_code=200, response_model=ResponseModel)
def get_random_recipe(
    api_choice: str, settings: Annotated[Settings, Depends(get_settings)]
):
    response = invoke_random_recipe(api_choice, settings)
    return response


@app.get("/recipes/cuisine", status_code=200, response_model=ResponseModel)
def get_recipes_by_cuisine(
    api_choice: str,
    settings: Annotated[Settings, Depends(get_settings)],
    input_cuisine: str,
    number_of_recipes: int = 1,
):
    response = invoke_recipes_by_cuisine(api_choice, settings, \
                                         input_cuisine, number_of_recipes)
    return response


@app.get("/recipes/ingredients", status_code=200, response_model=ResponseModel)
def get_recipes_by_ingredients(
    api_choice: str,
    settings: Annotated[Settings, Depends(get_settings)],
    selected_ingredients: str = Query(None),
    custom_ingredients: str = Query(None),
    number_of_recipes: int = 1,
):
    response = invoke_recipes_by_ingredients(api_choice, settings, \
                    selected_ingredients, custom_ingredients, number_of_recipes)
    return response


@app.get("/recipes/mealcourse", status_code=200, response_model=ResponseModel)
def get_recipes_by_mealcourse(
    api_choice: str,
    settings: Annotated[Settings, Depends(get_settings)],
    mealcourse: str,
    number_of_recipes: int = 1
):
    response = invoke_recipes_by_mealcourse(api_choice, settings, \
                    mealcourse, number_of_recipes)
    return response