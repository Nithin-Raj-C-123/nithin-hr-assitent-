import streamlit as st

with open("chatagent.html", "r", encoding="utf-8") as f:  # put the real name here
    html_code = f.read()

st.components.v1.html(html_code, height=800)
