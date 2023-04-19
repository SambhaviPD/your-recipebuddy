import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/recipes/random/"

st.set_page_config(page_title="Random Recipe", page_icon="🍲")

st.markdown("## Who does not love surprises?")

st.markdown(
    "#### Not sure what to cook?  \
    Why don't you let the app suggest something out of the blue 😉"
)

with st.form("surpriseme_form"):
    submitted = st.form_submit_button("Surprise me!")

    if submitted:
        API_URL = f"{API_URL}?api_choice=Spoonacular"
        response = requests.get(API_URL)
        output = response.json()
        st.write(output["message"])
        st.write(output["data"]
        )


