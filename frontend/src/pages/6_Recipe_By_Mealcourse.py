import requests

import streamlit as st

API_URL = "http://127.0.0.1:8000/recipes/{mealcourse}"

st.set_page_config(
    page_title="By Meal course",
    page_icon="🍧"
)

st.markdown("### Do you like to see some healthy starters, or yummy desserts, or a filling main course?")

mealcourse = st.selectbox("Choose any one below: ", 
             ("Starters", "Soups", "Main Course", "Desserts"))

st.selectbox("How many recipes would you like to see?",
             (1, 2, 3, 4, 5))

with st.form("recipebymealcourse_form"):
    submitted = st.form_submit_button("Fetch some recipes")

    if submitted:
        response = requests.get(API_URL)
        output = response.json()
        st.write(output["message"])