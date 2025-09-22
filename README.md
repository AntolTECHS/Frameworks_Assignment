# Frameworks_Assignment

Interactive exploration of COVID-19 research papers from the CORD-19 dataset.

---

##  Frameworks_Assignment/
├── data/                # Contains metadata.csv (not included in repo)
├── outputs/             # Generated plots
├── scripts/
│   ├── app.py           # Streamlit app
│   └── explore_data.py  # Data exploration script
├── src/
│   ├── __init__.py      # Makes src a Python package
│   └── data_prep.py     # Data loading and cleaning functions
├── venv/                # Python virtual environment
├── README.md
└── REPORT.md


---

## ⚡ Setup Instructions

1. **Clone the repo**
```bash
git clone <your_repo_url>
cd Frameworks_Assignment


##  Create virtual environment

python3 -m venv venv
source venv/bin/activate


##  Install required packages

pip install -r requirements.txt


##  Download dataset

Register on Kaggle and download metadata.csv from:
CORD-19 dataset

Place it in the data/ folder.


##  Run data exploration script

python -m scripts.explore_data

Plots will be saved in outputs/.


##Run Streamlit app

streamlit run scripts/app.py


## 📝 Notes

data/metadata.csv is ignored in Git to keep the repo small.

outputs/ contains generated plots.

Code is structured into scripts/ for execution and src/ for reusable functions.



---

### 📄 `REPORT.md`
```markdown
# Frameworks Assignment Report

## 1. Objective
- Explore the CORD-19 metadata dataset.
- Perform data cleaning and analysis.
- Visualize patterns in COVID-19 research papers.
- Build an interactive Streamlit application.

---

## 2. Data Loading
- Dataset: `metadata.csv` (20,000 sample rows used)
- Columns include titles, abstracts, publication dates, authors, journals, etc.
- Missing values handled for key columns:
  - `abstract` filled with empty strings
  - `publish_time` converted to datetime
  - `year` extracted for analysis
  - `abstract_word_count` computed

---

## 3. Data Cleaning
- Converted `publish_time` to `datetime`
- Extracted `year` column
- Filled missing abstracts
- Removed irrelevant ID columns (mag_id, arxiv_id, etc.)

---

## 4. Data Analysis & Visualizations
- **Publications by Year**: Most papers published in 2020-2021.
- **Top Journals**: Bar chart shows the 10 journals with highest COVID-19 publications.
- **Word Cloud**: Frequent words in paper titles highlight research focus areas.
- **Abstract Word Count Distribution**: Histogram shows typical paper lengths.

---

## 5. Streamlit App Features
- Year range slider to filter papers
- Dynamic visualizations based on selected range
- Word cloud of titles
- Sample of filtered dataset displayed

---

## 6. Challenges & Learnings
- Handling missing values in date and author fields
- Managing large dataset without storing it in Git
- Setting up Streamlit to find local modules (`src/`)
- Generating interactive visualizations for quick insight

---

## 7. Conclusion
- Successfully explored COVID-19 metadata
- Visualized research trends and top journals
- Built a functional Streamlit app
- Gained hands-on experience with pandas, matplotlib, seaborn, wordcloud, and Streamlit
