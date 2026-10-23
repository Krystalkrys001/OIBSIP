# Email Spam Detection with Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Task-Completed-brightgreen.svg)]()

This repository contains the implementation of **Task 4: Email Spam Detection**, completed as part of the **Oasis Infobyte Data Science Internship (OIBSIP)** program.

---

## 📌 Project Overview

Email communication is a core tool in modern daily interactions, but it is frequently susceptible to spam messages containing phishing attempts, promotional clutter, or malicious links. This project leverages Machine Learning and Natural Language Processing (NLP) techniques in Python to automatically classify incoming messages into two distinct categories:

- **Ham**: Legitimate, personal, or transactional messages.
- **Spam**: Unsolicited, promotional, or deceptive messages.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python
- **Data Manipulation:** pandas, numpy
- **Data Visualization:** matplotlib, seaborn, wordcloud
- **Machine Learning & NLP:** scikit-learn (CountVectorizer, TF-IDF, Naive Bayes, Logistic Regression, SVM)

---

## 🔍 Exploratory Data Analysis & Key Insights

1. **Class Distribution:** Analyzed the proportion of legitimate (ham) vs. unwanted (spam) messages to handle class imbalance appropriately.
2. **Text Feature Analysis:** Extracted word frequencies and key features across categories.
3. **Word Cloud Visualizations:**
   - **Ham Messages (Blue):** Predominated by conversational, everyday vocabulary such as ok, got, come, love, time, good, and need.
   - **Spam Messages (Red/Dark):** Predominated by high-urgency and promotional keywords such as free, call, text, reply, mobile, `prize, cash, and urgent.

---

## 🚀 Repository Structure

```text
OIBSIP/
└── DataScience-Task4-EmailSpamDetection/
    ├── spam.csv                        # Dataset
    ├── email_spam_detection.ipynb      # Main Jupyter Notebook implementation
    ├── README.md                       # Repository Documentation
    └── Project_Report.md               # Detailed Data Science Report
```

---

## 💻 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/OIBSIP.git
   cd OIBSIP/DataScience-Task4-EmailSpamDetection
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn wordcloud
   ```

3. **Run the Notebook:**
   Open `email_spam_detection.ipynb` in Jupyter Notebook or Google Colab and run all cells.

---

## 👤 Author
- **Program:** Oasis Infobyte Data Science Internship (OIBSIP)
- **Track:** Data Science
- **Task:** Task 4 – Email Spam Detection
