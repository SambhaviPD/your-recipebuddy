import re
from playwright.sync_api import Page, expect

def test_homepage_has_RecipeBuddy_in_title_and_all_subpages_linked_correctly(page: Page):
    page.goto("http://localhost:8501/")

    # Expect a title "to contain" a substring
    expect(page).to_have_title(re.compile("Recipe Buddy"))

    page_content = page.text_content("body")

    expect(page_content).to_contain_text("Just click on a menu")

    # create a locator
    random_recipe = page.get_by_role("link", name="Random Recipe")

    # Click the random recipe link
    random_recipe.click()

    # Expect the url to contain Random_Recipe
    expect(page).to_have_url(re.compile("/Random_Recipe"))

    # Recipe By Cuisine sub page related
    recipe_by_cuisine = page.get_by_role("link", name="Recipe By Cuisine")

    recipe_by_cuisine.click()

    expect(page).to_have_url(re.compile("/Recipe_By_Cuisine"))

    # Recipe By Ingredients sub page related
    recipe_by_ingredients = page.get_by_role("link", name="Recipe By Ingredients")

    recipe_by_ingredients.click()

    expect(page).to_have_url(re.compile("/Recipe_By_Ingredients"))

    # Recipe By Meal Course sub page related
    recipe_by_mealcourse = page.get_by_role("link", name="Recipe By Mealcourse")

    recipe_by_mealcourse.click()

    expect(page).to_have_url(re.compile("/Recipe_By_Mealcourse"))

    # TODO - How to check for content in a page
