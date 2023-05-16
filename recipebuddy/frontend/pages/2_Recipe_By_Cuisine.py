import requests
import streamlit as st

API_URL = "http://backend:8080/recipes/cuisine"

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
        API_URL = f"{API_URL}?api_choice=Spoonacular&input_cuisine={cuisine_option}&input_results={results_option}"
        response = requests.get(API_URL)
        output = response.json()
        st.write(output["message"])
        st.write(output["data"])