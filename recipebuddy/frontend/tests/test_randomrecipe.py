import re
from playwright.sync_api import Page, expect, sync_playwright

def test_randomrecipe_page_in_title(page: Page):
    page.goto("http://localhost:8501/Random_Recipe")

    #Expect a title "to contain" a substring
    expect(page).to_have_title(re.compile("Random Recipe"))

    