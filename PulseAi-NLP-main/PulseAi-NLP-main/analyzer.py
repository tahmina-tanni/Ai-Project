import nltk_setup
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sia = SentimentIntensityAnalyzer()

# ---- SENTIMENT ANALYSIS ----
def get_sentiment(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        return "Positive", compound
    elif compound <= -0.05:
        return "Negative", compound
    else:
        return "Neutral", compound

# ---- KEYWORD EXTRACTION ----
def get_keywords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    keywords = [w for w in tokens if w.isalpha() and w not in stop_words]
    return list(set(keywords))

# ---- COMPLAINT CATEGORY ----
def get_category(text):
    text = text.lower()

    delivery_words = ['delivery', 'late', 'delayed', 'slow', 'shipping', 'arrived']
    service_words = ['staff', 'rude', 'service', 'behaviour', 'unhelpful', 'ignored']
    quality_words = ['quality', 'broken', 'damaged', 'bad', 'terrible', 'worst', 'defective']
    pricing_words = ['expensive', 'price', 'overpriced', 'costly', 'cheap', 'refund']

    if any(word in text for word in delivery_words):
        return "🚚 Delivery Issue"
    elif any(word in text for word in service_words):
        return "😤 Service Problem"
    elif any(word in text for word in quality_words):
        return "📦 Product Quality Issue"
    elif any(word in text for word in pricing_words):
        return "💰 Pricing Issue"
    else:
        return "✅ General Feedback"