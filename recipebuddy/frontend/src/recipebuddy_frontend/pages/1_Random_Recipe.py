import os
import requests
import streamlit as st

API_URL = f"{os.environ.get('API_BASE_URL')}/recipes/random"

st.set_page_config(page_title="Random Recipe", page_icon="🍲")

st.markdown("## Who does not love surprises?")

st.markdown(
    "#### Not sure what to cook?  \
    Why don't you let the app suggest something out of the blue 😉"
)

with st.form("surpriseme_form"):
    submitted = st.form_submit_button("Surprise me!")

    if submitted:
        API_URL = f"{API_URL}"
        response = requests.get(API_URL)
        output = response.json()
        html_response = (output["data"]["choices"][0]["message"]["content"])
        st.components.v1.html(html_response, height=1000)
        


