import os
import requests
import streamlit as st

API_URL = f"{os.environ.get('API_BASE_URL')}/recipes/cuisine"

st.set_page_config(page_title="By Cuisine", page_icon="🥘")

st.markdown("### Choose your favorite Cuisine")

cuisine_option = st.selectbox(    
    "Choose a Cuisine:",
    ("African", "Asian", "American", "British", "Cajun", \
     "Caribbean", "Chinese", "Eastern European", "European", \
     "French", "German", "Greek", "Indian", "Irish", "Italian", \
     "Japanese", "Jewish", "Korean", "Latin American", "Mediterranean", \
     "Mexican", "Middle Eastern", "Nordic", "Southern", "Spanish", \
     "Thai", "Vietnamese"),
    key="cuisine_selectbox"
)

number_of_recipes =st.selectbox(
    "How many recipes do you want to see?",
    (1,2,3),
    key="results_selectbox"
)

with st.form("recipebycuisine_form"):
    submitted = st.form_submit_button("Fetch Recipe!")

    if submitted:
        API_URL = f"{API_URL}?api_choice=Spoonacular&input_cuisine={cuisine_option}&number_of_recipes={number_of_recipes}"
        response = requests.get(API_URL)
        output = response.json()
        st.write(output["message"])
        st.write(output["data"])