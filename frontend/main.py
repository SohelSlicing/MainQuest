import streamlit as st
import requests

st.set_page_config(page_title="MainQuest", page_icon="frontend/assets/logo.jpg")

# Header with logo
st.header("MainQuest")



if st.button("Send get request"):
    res = requests.get(url = url)
    st.write(res.text)