import requests

import streamlit as st

st.set_page_config(page_title="By Ingredients", page_icon="🥦")

st.markdown("## What main ingredients do you have today? ")

selected_ingredients = st.multiselect("Select one or more from the list", 
               ("Brocoli", "Cheese", "Meat", "Mushroom", "Pasta", "Tomato")
               )

st.markdown("#### We know we cannot show all possibe ingredients. \
            So feel free to type below.")

custom_ingredients = st.text_area("Type your ingredients separated by a comma", \
                                  placeholder="lettuce, flour, olives")

results_option = st.selectbox(
    "How many recipes do you want to see?",
    (1,2,3,4,5)
)

with st.form("recipebyingredient_form"):
    submitted = st.form_submit_button("Fetch Recipe")

    if submitted:
        selected_ingredients = str(selected_ingredients)
        # Remove additional white spaces
        custom_ingredients = custom_ingredients.replace(", ", ",")
        results_option = str(results_option)
        
        API_URL = f"http://backend:8080/recipes/ingredients?api_choice=Spoonacular&selected_ingredients={selected_ingredients}&custom_ingredients={custom_ingredients}&number_of_recipes={results_option}"
        
        response = requests.get(API_URL)
        output = response.json()
        st.write(output["message"])
        st.write(output["data"])
