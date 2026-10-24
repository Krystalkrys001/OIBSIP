# Task 5: Sales Prediction Using Python (Regression & Business Impact)

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Task-Completed-brightgreen.svg)]()

This repository contains the complete implementation for **Task 5: Sales Prediction Using Python**, completed as part of the **Oasis Infobyte Data Science Internship (OIBSIP)** program.

---

## 📌 Project Overview & Strategic Business Impact

In commercial enterprises, allocating marketing budgets across various media channels (TV, Radio, Newspaper) directly impacts top-line revenue. This project builds an Ordinary Least Squares (OLS) Multiple Linear Regression framework to predict product sales based on advertising spend while analyzing marketing attribution and channel-specific ROI.

Rather than focusing solely on raw accuracy metrics, this project highlights **business interpretability**, **coefficient attribution**, and **residual error diagnostics** to guide executive decision-making on budget allocation.

---

## 📊 Dataset Profile & Summary Statistics

* **Dataset:** `Advertising.csv`
* **Total Observations:** 200 rows, 4 clean variables (after dropping the redundant index column `Unnamed: 0`).
* **Missing Values:** 0 null entries (100% complete data).

### Feature Breakdown

| Feature | Type | Units | Mean | Std Dev | Min | Max | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TV** | Feature | $1,000s | $147.04 | $85.85 | $0.70 | $296.40 | Advertising budget spent on TV campaigns |
| **Radio** | Feature | $1,000s | $23.26 | $14.85 | $0.00 | $49.60 | Advertising budget spent on Radio campaigns |
| **Newspaper** | Feature | $1,000s | $30.55 | $21.78 | $0.30 | $114.00 | Advertising budget spent on Newspaper ads |
| **Sales** | **Target** | 1,000 units | 14.02 | 5.22 | 1.60 | 27.00 | Product sales volume |

---

## 📈 Exploratory Data Analysis (EDA) Insights

1. **Correlation Matrix Analysis:**
   * **TV vs. Sales ($r = 0.782$):** Strongest linear correlation. TV serves as the primary engine for driving total sales volume.
   * **Radio vs. Sales ($r = 0.576$):** Moderate-to-strong positive correlation, indicating high efficiency per dollar spent.
   * **Newspaper vs. Sales ($r = 0.228$):** Weak correlation, indicating low effectiveness relative to TV and Radio.
   * **Multicollinearity:** Inter-feature correlations remain low (maxing out at $0.354$ between Radio and Newspaper), satisfying the linear regression assumption of independent predictors.

2. **Visual Observations:**
   * **Scatter Plots:** Sales vs. TV exhibits a clear upward trend with minimal spread. Sales vs. Radio shows a consistent positive trajectory. Sales vs. Newspaper shows wide scatter with limited directionality.

---

## ⚙️ Model Architecture & Performance Results

* **Algorithm:** Multiple Linear Regression (OLS) via `scikit-learn`
* **Data Split:** 80% Train (160 rows), 20% Test (40 rows), `random_state=42`

### Performance Metrics on Test Set

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **$R^2$ Score** | **0.8994** | The model explains **89.94%** of the variance in product sales. |
| **RMSE** | **1.7816** | Average prediction deviation is ~1.78 thousand units. |

### Regression Formula & Coefficients

$$\text{Sales} = 2.9791 + (0.0447 \times \text{TV}) + (0.1892 \times \text{Radio}) + (0.0028 \times \text{Newspaper})$$

* **Radio Coefficient ($0.1892$):** **Highest marginal efficiency.** Holding TV and Newspaper constant, every $1,000 increase in Radio spend yields an estimated **189 additional units sold**.
* **TV Coefficient ($0.0447$):** **Volume Driver.** While the per-dollar weight is smaller, TV accounts for the bulk of absolute sales revenue due to higher budget scales.
* **Newspaper Coefficient ($0.0028$):** Statistically negligible return.

---

## 🔍 Model Diagnostics & Residual Analysis

* **Residual Spread:** The residual plot (Predicted Sales vs. Errors) displays errors distributed around the zero line ($y = 0$).
* **Homoscedasticity:** Error variance stays consistent across most predicted values, with slight non-linear curvature at higher spends indicating mild diminishing marginal returns.

---

## 📁 Repository Structure

```text
OIBSIP/
└── DataScience-Task5-SalesPrediction/
    ├── Advertising.csv            # Cleaned raw dataset (200 rows x 4 columns)
    ├── Advertising.ipynb          # Jupyter Notebook with complete workflow
    ├── README.md                  # Project documentation
    └── Project_Report.md          # In-depth executive & analytical report
```

---

## 🛠️ Environment & Setup

```bash
# Clone repository
git clone https://github.com/your-username/OIBSIP.git
cd OIBSIP/DataScience-Task5-SalesPrediction

# Ensure compatible dependencies
pip install "numpy<2" pandas matplotlib seaborn scikit-learn
```

---

## 👤 Author
* **Program:** Oasis Infobyte Data Science Internship (OIBSIP)
* **Track:** Data Science
* **Task:** Task 5 – Sales Prediction Using Python