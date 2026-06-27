import streamlit as st
import joblib

# Page Configuration
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

# Custom Background & Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
}

.main-title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #dcdcdc;
    font-size: 18px;
}

.result-box {
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Load Model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Heading
st.markdown(
    '<p class="main-title">📰 Fake News Detector</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Machine Learning Based News Classification System</p>',
    unsafe_allow_html=True
)

st.write("---")

# Input
news = st.text_area(
    "Enter News Headline",
    placeholder="Type or paste a news headline here..."
)

# Prediction
if st.button("🔍 Predict News"):

    if news.strip() == "":
        st.warning("Please enter a news headline.")
    else:
        news_vector = vectorizer.transform([news])
        prediction = model.predict(news_vector)

        if prediction[0] == 1:
            st.success("✅ REAL NEWS")
        else:
            st.error("❌ FAKE NEWS")

st.write("---")
st.caption("Developed using Python, Streamlit, TF-IDF and Logistic Regression")