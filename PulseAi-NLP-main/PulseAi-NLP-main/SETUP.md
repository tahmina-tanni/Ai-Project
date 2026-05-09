# PulseAi-NLP — Setup Guide

---

## Step 1 — Git Init & Push

- Run one by one in terminal:

- git init
- git add .
- git commit -m "initial commit - PulseAi Customer Sentiment Tracker"


Go to [GitHub.com](https://github.com):
- Click **New Repository**
- Name it: `PulseAi-NLP`
- Set **Public**
- **Do NOT** check "Add README"
- Click **Create Repository**

Back in terminal:

- git remote add origin https://github.com/YOUR_USERNAME/PulseAi-NLP.git
- git branch -M main
- git push -u origin main

---

## Step 2 — Install Packages

- pip install streamlit textblob nltk plotly pandas streamlit-option-menu


- Create NLTK folder on D drive and download data:

- mkdir D:\nltk_data

- python -c "import nltk; nltk.data.path.append('D:/nltk_data'); nltk.download('vader_lexicon', download_dir='D:/nltk_data'); nltk.download('punkt', download_dir='D:/nltk_data'); nltk.download('stopwords', download_dir='D:/nltk_data')"


- Download TextBlob corpora:

- python -m textblob.download_corpora


---

## Step 3 — NLTK Setup File

- Create file `nltk_setup.py` in project folder:

- import nltk
- nltk.data.path.append('D:/nltk_data')


---

## Step 4 — Clean requirements.txt

- echo streamlit> requirements.txt & echo textblob>> requirements.txt & echo nltk>> requirements.txt & echo plotly>> requirements.txt & echo pandas>> requirements.txt & echo streamlit-option-menu>> requirements.txt


---

## Step 5 — Run The App

- streamlit run app.py


---

## Project Structure


PulseAi-NLP/
├── app.py
├── sidebar.py
├── nltk_setup.py
├── analyzer.py
├── home.py
├── feedback_page.py
├── requirements.txt
├── SETUP.md
└── images/
    ├── positive.png
    ├── negative.png
    └── neutral.png