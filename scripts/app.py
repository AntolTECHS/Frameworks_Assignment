# scripts/app.py

import sys
import os
# Ensure parent directory is in sys.path so src can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from src.data_prep import load_metadata, clean_metadata

# --- Load data ---
@st.cache_data
def get_data(nrows=20000):
    df = load_metadata("data/metadata.csv", nrows=nrows)
    return clean_metadata(df)

df = get_data()

# --- App Layout ---
st.title("📊 CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers (sample from metadata.csv).")

# Year range slider
min_year, max_year = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select publication year range:",
                       min_year, max_year, (2020, 2021))

# Filter data
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

st.write(f"Showing **{len(filtered_df)} papers** from {year_range[0]} to {year_range[1]}")

# --- Visualization 1: Publications by Year ---
st.subheader("Publications by Year")
year_counts = filtered_df["year"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8, 4))
year_counts.plot(kind="bar", ax=ax)
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# --- Visualization 2: Top Journals ---
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8, 4))
top_journals.plot(kind="bar", ax=ax)
ax.set_title("Top Journals Publishing COVID-19 Research")
ax.set_xlabel("Journal")
ax.set_ylabel("Count")
st.pyplot(fig)

# --- Visualization 3: Word Cloud of Titles ---
st.subheader("Word Cloud of Paper Titles")
titles_text = " ".join(filtered_df["title"].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles_text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# --- Sample of the Data ---
st.subheader("Sample Data")
st.dataframe(filtered_df.head(20))
