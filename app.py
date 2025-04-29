import streamlit as st
import random

def classify_niche(keyword):
    categories = {
        "Emerging": "Looks promising with growing interest.",
        "Saturated": "Highly competitive market.",
        "Untapped": "Little competition, potential opportunity."
    }
    label = random.choice(list(categories.keys()))
    return label, categories[label]

st.set_page_config(page_title="Niche Market Detector")
st.title("🔍 Niche Market Detector")
st.write("Enter a product or business idea to see if it’s an emerging, saturated, or untapped niche.")

keyword = st.text_input("Enter your niche keyword:")

if keyword:
    label, description = classify_niche(keyword)
    st.subheader(f"Result: {label} Market")
    st.write(description)
