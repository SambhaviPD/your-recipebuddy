import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/recipes/{cuisine}"

st.set_page_config(page_title="By Cuisine", page_icon="🥘")

st.markdown("### Choose your favorite Cuisine")

cuisine_option = st.selectbox(
    "Pick one to start with:",
    ("Chinese", "Continental", "Indian", "Sushi", "Thai")
)

results_option =st.selectbox(
    "How many recipes do you want to see?",
    (1,2,3,4,5)
)

with st.form("recipebycuisine_form"):
    submitted = st.form_submit_button("Fetch Recipe!")

    if submitted:
        response = requests.get(API_URL)
        output = response.json()
        st.write(output["message"])