import requests
import re

from playwright.sync_api import Page, expect

def test_page_title(page: Page):
    page.goto("http://localhost:8501/Random_Recipe")

    expect(page).to_have_title(re.compile("Random Recipe"))


def test_page_static_content(page: Page):
    page.goto("http://localhost:8501/Random_Recipe")

    expected_string1 = "Why don't you let the app suggest something"
    
    expect(page.get_by_text(expected_string1)).to_be_visible()

    expected_string2 = "Who does not love surprises?"

    expect(page.get_by_text(expected_string2)).to_be_visible()


def test_page_successful_response(page: Page):
    page.goto("http://localhost:8501/Random_Recipe")

    API_URL = "http://localhost:8080/recipes/random"
    API_URL = f"{API_URL}?api_choice=Spoonacular"

    response = requests.get(API_URL)
    page.wait_for_timeout(5000)

    expected_response = "Successfully returned a random recipe. Enjoy!"
    assert response.json()["message"] in expected_response
