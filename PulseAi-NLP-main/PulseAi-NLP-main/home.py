import streamlit as st

def renderPage():
    st.markdown("# 🧠 PulseAi")
    st.markdown("### Customer Sentiment Tracker")
    st.markdown("---")

    st.markdown("""
    Welcome to **PulseAi** — a smart customer feedback analysis tool 
    designed for small and medium businesses.
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("💬 **Sentiment Analysis**\n\nDetects if customer feedback is Positive, Negative or Neutral")

    with col2:
        st.warning("📂 **Complaint Detection**\n\nIdentifies Delivery, Service, Quality or Pricing issues")

    with col3:
        st.success("🔑 **Keyword Extraction**\n\nExtracts important words from customer reviews")

    st.markdown("---")

    st.markdown("### How It Works")

    st.markdown("""
    1. Go to **Analyze Feedback** from the sidebar
    2. Type or paste a customer review
    3. Click **Analyze**
    4. Instantly get Sentiment, Category and Keywords
    """)

    st.markdown("---")

    st.markdown("### Example")

    st.code("""
Review   : "The food was good but delivery was very slow."

Sentiment : Neutral
Category  : Delivery Issue
Keywords  : food, delivery, slow
    """)

    st.markdown("---")
    st.caption("PulseAi — Built with Python, Streamlit, NLTK, TextBlob & Vader")