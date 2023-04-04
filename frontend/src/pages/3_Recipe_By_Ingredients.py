import requests

import streamlit as st

API_URL = "http://127.0.0.1:8000/recipes/{ingredients}"

st.set_page_config(page_title="By Ingredients", page_icon="🥦")

st.markdown("## What main ingredients do you have today? ")

selected_ingredients = st.multiselect("Select one or more from the list", 
               ("Brocoli", "Cheese", "Meat", "Mushroom", "Pasta", "Tomato")
               )

st.markdown("#### We know we cannot show all possibe ingredients. \
            So feel free to type below.")

custom_ingredients = st.text_area("Type your ingredients separated by a comma", placeholder="lettuce, flour, olives")

results_option = st.selectbox(
    "How many recipes do you want to see?",
    (1,2,3,4,5)
)

with st.form("recipebyingredient_form"):
    submitted = st.form_submit_button("Fetch Recipe")

    if submitted:
        response = requests.get(API_URL)
        output = response.json()
        st.write(output["message"])
