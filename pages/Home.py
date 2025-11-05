import streamlit as st
import pandas as pd

st.set_page_config(page_title="Home", page_icon=":material/home:")

st.title("Streamlit Playground — MacBook IDE")

st.warning("This theming is from: https://doc-theming-overview-anthropic-light-inspired.streamlit.app/ ")

option = st.selectbox(
    "Who helped you setting this up?",
    ("My Cat", "My Dog", "ChatGPT", "Mum"),
)

st.write("You selected:", option)