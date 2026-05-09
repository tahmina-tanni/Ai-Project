import streamlit as st
from streamlit_option_menu import option_menu

def show():
    with st.sidebar:
        st.markdown("# 🧠 PulseAi")
        st.markdown("#### Customer Sentiment Tracker")
        st.markdown("---")
        selected = option_menu(
            menu_title=None,
            options=["🏠 Home", "📝 Analyze Feedback"],
            icons=["house", "chat-left-text"],
            default_index=0,
        )
        st.markdown("---")
        st.caption("Built with TextBlob + Vader + NLTK")
        return selected