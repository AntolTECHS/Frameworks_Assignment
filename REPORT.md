# Frameworks Assignment Report

## 1. Objective
- Explore the CORD-19 metadata dataset containing COVID-19 research papers.
- Perform data cleaning and preparation for analysis.
- Generate visualizations to identify trends and insights.
- Build an interactive Streamlit application for data exploration.

---

## 2. Data Overview
- Dataset: `metadata.csv` from CORD-19 (20,000 sample rows used).
- Key columns:
  - `title`, `abstract`, `authors`, `journal`, `publish_time`, `year`
  - IDs: `cord_uid`, `doi`, `pmcid`, etc.
- Some columns had missing values:
  - `publish_time` (940 missing)
  - `authors` (1019 missing)
  - `journal` (341 missing)

---

## 3. Data Cleaning
- Converted `publish_time` to `datetime`.
- Extracted publication `year`.
- Created `abstract_word_count` for basic text analysis.
- Dropped irrelevant or empty columns (`mag_id`, `arxiv_id`, `s2_id`, etc.).
- Filled or handled missing data where necessary.

---

## 4. Exploratory Data Analysis
### 4.1 Publications by Year
- Most papers were published in 2020 and 2021.
- Year distribution shows surge in COVID-19 research after the pandemic began.

### 4.2 Top Journals
- Top 10 journals publishing COVID-19 papers were identified using a bar chart.
- Shows which journals contributed most to the research.

### 4.3 Word Cloud of Titles
- Frequent words include “COVID”, “SARS-CoV-2”, “pandemic”, etc.
- Visualizes research focus areas effectively.

### 4.4 Abstract Word Count
- Abstracts range widely in length.
- Histogram provides insight into typical paper length.

---

## 5. Streamlit Application
- Interactive slider to select year range for filtering.
- Updates visualizations dynamically based on selection.
- Displays:
  - Publications by year (bar chart)
  - Top journals (bar chart)
  - Word cloud of paper titles
  - Sample of filtered data in a table
- Provides intuitive exploration of research trends.

---

## 6. Challenges & Learning
- Handling missing and inconsistent data.
- Managing a large dataset without including it in Git.
- Setting up imports correctly for `src/` in Streamlit.
- Creating clear and meaningful visualizations.
- Using Streamlit caching to speed up app performance.

---

## 7. Conclusion
- Successfully cleaned, analyzed, and visualized COVID-19 research metadata.
- Built a functional and interactive Streamlit app for data exploration.
- Gained hands-on experience with:
  - Python (pandas, matplotlib, seaborn)
  - Data cleaning and preprocessing
  - Visualization and word cloud generation
  - Streamlit app development
