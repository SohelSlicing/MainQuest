import streamlit as st

from pages import flashcard

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar.radio(
        app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()

st.set_page_config(page_title="MainQuest", page_icon="frontend/assets/logo.jpg")

# Header with logo
col1, col2 = st.columns([1, 6])
col1.image("frontend/assets/logo.jpg", width=100)
col2.header("MainQuest")
