import streamlit as st
import pandas as pd

st.title("Streamlit Playground — MacBook VS Environment")

option = st.selectbox(
    "Who helped you setting this up?",
    ("ChatGPT via Atlas", "Tim", "My Cat"),
)

st.write("You selected:", option)
