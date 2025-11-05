import streamlit as st

pages = {
    "Main": [
        st.Page("pages/Home.py", title="Home", icon=":material/home:"),
        st.Page("pages/Text.py", title="Text", icon=":material/chat:"),
    ],
    "Details": [
        st.Page("pages/Widgets.py", title="Widgets", icon=":material/widgets:"),
        st.Page("pages/TA_Library.py", title="Technical Analysis", icon=":material/insert_chart:"),
],
}

pg = st.navigation(pages, position="top")
pg.run()