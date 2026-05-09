import streamlit as st
import streamlit.components.v1 as components
from analyzer import get_sentiment, get_keywords, get_category
from PIL import Image

def renderPage():
    st.markdown("# 📝 Analyze Feedback")
    st.markdown("### Customer Feedback Intelligence")
    components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)

    st.markdown("Enter a customer review below and click **Analyze** to get instant insights.")
    st.text("")

    userText = st.text_area("Customer Review", placeholder="e.g. The delivery was very slow but the product quality was excellent.", height=150)

    st.text("")

    if st.button("🔍 Analyze"):
        if userText.strip() != "":

            # ---- GET RESULTS ----
            sentiment, score = get_sentiment(userText)
            keywords = get_keywords(userText)
            category = get_category(userText)

            # ---- DISPLAY RESULTS ----
            st.markdown("---")
            st.markdown("## 📊 Results")

            # sentiment image
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### Sentiment")
                if sentiment == "Positive":
                    st.success(f"😊 {sentiment}")
                    image = Image.open('./images/positive.png')
                elif sentiment == "Negative":
                    st.error(f"😔 {sentiment}")
                    image = Image.open('./images/negative.png')
                else:
                    st.warning(f"😐 {sentiment}")
                    image = Image.open('./images/neutral.png')
                st.image(image, width=100)

            with col2:
                st.markdown("### Category")
                st.info(f"{category}")
                st.markdown("### Compound Score")
                st.metric(label="Vader Score", value=round(score, 2))

            with col3:
                st.markdown("### Keywords")
                if keywords:
                    for kw in keywords[:8]:
                        st.markdown(f"- `{kw}`")
                else:
                    st.write("No keywords found.")

            # ---- SUMMARY BOX ----
            st.markdown("---")
            st.markdown("### 📋 Summary")
            st.markdown(f"""
            | Field | Result |
            |---|---|
            | **Sentiment** | {sentiment} |
            | **Category** | {category} |
            | **Vader Score** | {round(score, 2)} |
            | **Keywords** | {", ".join(keywords[:8])} |
            """)

        else:
            st.warning("⚠️ Please enter a customer review first.")