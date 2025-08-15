# granite_utils.py
import os
from dotenv import load_dotenv
from langchain_community.llms import Replicate

load_dotenv()

def get_granite_model():
    api_token = os.getenv("REPLICATE_API_TOKEN")
    if not api_token:
        raise ValueError("REPLICATE_API_TOKEN tidak ditemukan di .env")

    return Replicate(
        model="ibm-granite/granite-3.2-8b-instruct",
        replicate_api_token=api_token
    )

# Bersihkan label supaya hanya positive / negative
def clean_sentiment_label(label: str) -> str:
    label = label.strip().lower()
    if label in ["positive", "pos"]:
        return "positive"
    elif label in ["negative", "neg"]:
        return "negative"
    else:
        return "negative"  # fallback kalau Granite ngaco

def granite_sentiment(text: str) -> str:
    model = get_granite_model()
    prompt = (
        "Classify the sentiment of this text strictly as 'Positive' or 'Negative'.\n"
        "Do not use Neutral or Mixed.\n\n"
        f"Text: {text}"
    )
    result = model.invoke(prompt)
    return clean_sentiment_label(result.split()[0])  # ambil kata pertama

def granite_summary(text: str) -> str:
    model = get_granite_model()
    prompt = f"Summarize the following text in 3 sentences:\n\n{text}"
    return model.invoke(prompt)

def granite_keywords(text: str) -> str:
    model = get_granite_model()
    prompt = f"Extract 5 main keywords from the following text:\n\n{text}"
    return model.invoke(prompt)
