import os
import matplotlib.pyplot as plt
from src.data_prep import load_metadata, clean_metadata

# Ensure outputs/ folder exists
os.makedirs("outputs", exist_ok=True)

# Load and clean
df = load_metadata("data/metadata.csv", nrows=20000)
df = clean_metadata(df)

print("Shape:", df.shape)
print(df.info())
print("Missing values:\n", df.isnull().sum().head())

# --- Visualization 1: Publications by year ---
year_counts = df["year"].value_counts().sort_index()
plt.figure(figsize=(10, 5))
year_counts.plot(kind="bar")
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/publications_by_year.png")
plt.close()

# --- Visualization 2: Top journals ---
top_journals = df["journal"].value_counts().head(10)
plt.figure(figsize=(10, 5))
top_journals.plot(kind="bar")
plt.title("Top Journals Publishing COVID-19 Research")
plt.xlabel("Journal")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/top_journals.png")
plt.close()

# --- Visualization 3: Abstract word count distribution ---
plt.figure(figsize=(10, 5))
df["abstract_word_count"].plot(kind="hist", bins=50)
plt.title("Distribution of Abstract Word Counts")
plt.xlabel("Word Count")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("outputs/abstract_word_counts.png")
plt.close()

print("✅ Plots saved in outputs/ folder")
