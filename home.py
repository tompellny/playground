import streamlit as st
import pandas as pd

st.title("Playground for Streamlit")

option = st.selectbox(
    "Who helped you setting this up?",
    ("ChatGPT via Atlas", "Tim", "My Cat"),
)

st.write("You selected:", option)
