import nltk_setup
import streamlit as st
import sidebar
import home
import feedback_page

st.set_page_config(
    page_title="PulseAi - Customer Sentiment Tracker",
    page_icon="🧠",
    layout="wide"
)

page = sidebar.show()

if page == "🏠 Home":
    home.renderPage()

elif page == "📝 Analyze Feedback":
    feedback_page.renderPage()