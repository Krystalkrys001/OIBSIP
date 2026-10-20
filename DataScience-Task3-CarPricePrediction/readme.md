# Car Price Prediction with Machine Learning (OIBSIP Task 3)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Oasis Infobyte Data Science Fellowship (OIBSIP) — Task 3**  
> **Author:** Chukwuma Obinna Ulasi ([Portfolio Website](https://www.chukwumaulasi.com.ng) | [LinkedIn](https://www.linkedin.com/in/chukwuma-ulasi))  
> **Location:** Lagos, Nigeria  

---

## Project Overview
Accurate used car pricing is a vital asset for automotive e-commerce platforms, auto-financing fintechs, and insurance underwriters. This project builds a production-grade machine learning regression pipeline on the **Cardekho Dataset** (15,411 historical transaction records) to predict vehicle market prices based on physical specs, usage metrics, and brand positioning.

Comparing a baseline **Linear Regression** model against an ensemble **Random Forest Regressor**, the final pipeline achieves an **$R^2$ accuracy score of 0.9383 (93.83%)**, cutting average prediction errors down to under **₹100,000 (₦1.8M)**.

The project concludes with an **interactive Jupyter Dashboard Widget** that enables real-time valuation inputs with localized output conversion in **Indian Rupees (INR)** and **Nigerian Naira (NGN)**.

---

## Key Results & Model Performance

| Model Algorithm | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) | $R^2$ Score (Accuracy) |
| :--- | :--- | :--- | :--- |
| **Linear Regression (Baseline)** | ₹212,123.08 | ₹427,863.91 | `0.7473` (74.73%) |
| **Random Forest Regressor** | **₹99,796.98** | **₹211,364.70** | **`0.9383` (93.83%)** |

### Key Analytical Insights:
* **Top Value Driver:** Engine horsepower (`max_power`) contributes over **65%** of the relative predictive power in valuation.
* **Depreciation Decay:** `vehicle_age` and `km_driven` follow non-linear decay curves, which tree-based ensemble models capture significantly better than linear lines.
* **Outlier Auditing:** Identified and filtered severe data entry errors (e.g., a 5-year-old vehicle claiming 3.8 million kilometers driven).

---

## Interactive Dashboard Preview
The project includes a custom UI built using `ipywidgets` and HTML/CSS rendering inside Jupyter Notebooks:

```
+-----------------------------------------------------------------------+
| Used Car Price Predictor Dashboard                                 |
+------------------------------------+----------------------------------+
| Year: [=====o====================] | Engine (CC): [  1200  ]          |
| KM Driven: [ 50000 ]               | Max Power (BHP): [ 85.0 ]        |
| Mileage (km/L): [ 18.5 ]           | Fuel Type: [ Petrol         v ]  |
| Seats: [===o=====================] | Seller Type: [ Individual   v ]  |
| Transmission: [ Manual         v ] |                                  |
+------------------------------------+----------------------------------+
|               [ Calculate Estimated Value ]                           |
+-----------------------------------------------------------------------+
| 🚗 Valuation Complete!                                                |
| Estimated Market Value (INR): ₹550,000.00                             |
| Estimated Nigerian Market Value (NGN): ₦10,175,000.00                 |
+-----------------------------------------------------------------------+
```

---

## Repository Structure

```
OIBSIP/
└── DataScience-Task3-CarPricePrediction/
    ├── README.md                                   # Master Project Documentation
    ├── Task3_Car_Price_Prediction_Technical_Report.md # Comprehensive Technical Report
    ├── car_price_prediction_pipeline.py            # Complete Modular Python Pipeline
    ├── cardekho.ipynb                              # Interactive Jupyter Notebook
    ├── cardekho_dataset.csv                        # Dataset (15,411 rows)
    ├── car_price_model.pkl                         # Serialized Trained Random Forest Model
    └── model_columns.pkl                           # Serialized Feature Matrix Schema
```

---

## 🚀 Quickstart & Setup Guide

### 1. Prerequisites
Ensure Python 3.8+ is installed on your machine along with Jupyter Notebook or JupyterLab.

### 2. Clone Repository
```bash
git clone https://github.com/Krystalkrys001/OIBSIP.git
cd OIBSIP/DataScience-Task3-CarPricePrediction
```

### 3. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn ipywidgets
```

### 4. Enable Widget Extension (For Jupyter Notebook/Lab)
```bash
jupyter nbextension enable --py widgetsnbextension
```

### 5. Run Pipeline or Notebook
Execute the full automated Python script:
```bash
python car_price_prediction_pipeline.py
```
Or launch the interactive Jupyter Notebook:
```bash
jupyter notebook cardekho.ipynb
```

---

## 🤝 Acknowledgments
* **Oasis Infobyte (OIBSIP):** For providing the data science fellowship platform and project mandate.
* **Cardekho:** For the automotive transaction dataset.

---
*Created with passion by Chukwuma Obinna Ulasi — Lagos, Nigeria.*
