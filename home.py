import streamlit as st
import pandas as pd

st.title("Streamlit Playground — MacBook IDE")

option = st.selectbox(
    "Who helped you setting this up?",
    ("My Cat", "My Dog", "ChatGPT"),
)

st.write("You selected:", option)
