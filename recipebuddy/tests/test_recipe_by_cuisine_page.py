import re
import requests

from playwright.sync_api import Page, expect

def test_page_title(page: Page):
    page.goto("http://localhost:8501/Recipe_By_Cuisine")

    expect(page).to_have_title(re.compile("By Cuisine"))

def test_page_static_content(page: Page):
    page.goto("http://localhost:8501/Recipe_By_Cuisine")

    expected_string = "How many recipes do you want to see?"
    expected_string = expected_string.lower()

    page_content = page.text_content("body")
    page_content = page_content.lower()

    expect(page.get_by_text(expected_string)).to_be_visible()


#E2E test - Success flow
def test_page_successful_response(page: Page):
    page.goto("http://localhost:8501/Recipe_By_Cuisine")
    
    API_URL = "http://localhost:8080/recipes/cuisine"

    cuisine_value = "Indian"
    results_value = "3"

    API_URL = f"{API_URL}?api_choice=Spoonacular&input_cuisine={cuisine_value}&number_of_recipes={results_value}"
    print('API URL: ', API_URL)
    
    response = requests.get(API_URL)
    page.wait_for_timeout(5000)

    expected_response = "Successfully returned 3 Indian cuisine recipes"
    assert response.json()["message"] in expected_response

