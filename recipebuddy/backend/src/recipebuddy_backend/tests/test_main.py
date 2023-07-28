from fastapi.testclient import TestClient

from recipebuddy_backend.main import app

client = TestClient(app)

# Test the main route
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to Recipe Buddy!"

def test_fetch_random_recipes_using_spoonacular():
    response = client.get("/recipes/random",
                params={"api_choice" : "Spoonacular"})
    assert response.status_code == 200
    assert response.json()["message"] == "Successfully returned a random recipe. Enjoy!"


def test_fetch_random_recipes_without_using_spoonacular():
    response = client.get("/recipes/random",
                params={"api_choice" : "OpenAI"})
    assert response.status_code == 200
    assert response.json()["message"] == "Successfully returned a random recipe. Enjoy!"
