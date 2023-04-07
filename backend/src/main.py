from enum import Enum
from typing import List

from fastapi import FastAPI, UploadFile, Query

app = FastAPI(title="Recipe Buddy")


@app.get("/")
async def home():
    return "Welcome to Recipe Buddy!"


@app.get("/recipes/surpriseme/")
async def get_recipes_random():
    pass


class Cuisine(str, Enum):
    chinese = "chinese"
    continental = "continental"
    indian = "indian"
    sushi = "sushi"
    thai = "thai"


# @app.get("/recipes/{cuisine}")
# async def get_recipes_by_cuisine(cuisine: Cuisine):
#     pass


@app.get("/recipes/ingredients")
async def get_recipes_by_ingredients(selected_ingredients: str  = Query(None), \
                                     custom_ingredients: List[str] = Query(None), \
                                     number_of_recipes: str = Query(None)):
    return {"message" : f"Here are {number_of_recipes} recipes that uses {selected_ingredients} and {custom_ingredients}"}


@app.get("/recipes/{mealcourse}")
async def get_recipes_by_mealcourse(mealcourse: str):
    pass


# @app.get("/recipes/{image}")
# async def get_recipes_by_image(image: UploadFile):
#     pass


# @app.get("/recipes/{images}")
# async def get_recipe_by_images(images: UploadFile):
#     pass

