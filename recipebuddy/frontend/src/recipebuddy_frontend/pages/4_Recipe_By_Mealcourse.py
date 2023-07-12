import os
import requests

import streamlit as st

API_URL = f"{os.environ.get('API_BASE_URL')}/recipes/mealcourse"

st.set_page_config(
    page_title="By Meal course",
    page_icon="🍧"
)

st.markdown("### Do you like to see some healthy starters, or yummy desserts, or a filling main course?")

mealcourse = st.selectbox("Choose any one below: ", 
             ("Starters", "Soups", "Main Course", "Desserts"))

number_of_recipes = st.selectbox("How many recipes would you like to see?",
             (1, 2, 3, 4, 5))

with st.form("recipebymealcourse_form"):
    submitted = st.form_submit_button("Fetch some recipes")

    if submitted:
        API_URL = f"{API_URL}?api_choice=Spoonacular&mealcourse={mealcourse}&number_of_recipes={number_of_recipes}"
        response = requests.get(API_URL)
        output = response.json()
        st.write(output["message"])
        st.write(output["data"])