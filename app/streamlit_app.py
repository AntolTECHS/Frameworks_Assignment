import streamlit as st
import matplotlib.pyplot as plt
from src.data_prep import load_metadata, clean_metadata

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers metadata.")

@st.cache_data
def load_and_clean():
    df = load_metadata("data/metadata.csv", nrows=20000)
    return clean_metadata(df)

df = load_and_clean()

# Year filter
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", year_min, year_max, (2020, 2021))
filtered = df[df['year'].between(*year_range)]

# Publications over time
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index.astype(str), year_counts.values)
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
top_journals.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# Show sample
st.subheader("Sample Data")
st.dataframe(filtered[['title', 'authors', 'journal', 'year']].head(20))
