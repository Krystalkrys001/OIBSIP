# Comprehensive Technical Report: Car Price Prediction with Machine Learning
**Author:** Chukwuma Obinna Ulasi  
**Role:** Data Analyst & BI Specialist  
**Program:** Oasis Infobyte Data Science Fellowship (OIBSIP) — Task 3  
**Location:** Lagos, Nigeria  

---

## 1. Executive Summary & Business Context
In automotive retail, digital marketplaces, and auto-financing fintechs (e.g., Kuda Bank asset financing, Car45, Cars24), establishing fair market valuation for used vehicles is a core operational challenge. Manual pricing leads to valuation variance, mispriced loan collateral, and delayed inventory turnover.

This project implements an end-to-end predictive machine learning solution using the **Cardekho dataset** (15,411 historical vehicle transaction records across 14 attributes). By comparing a baseline linear parametric model against an ensemble tree-based algorithm, we achieved an **$R^2$ accuracy score of 0.9383 (93.83%)** using a **Random Forest Regressor**, successfully predicting vehicle market values within an average margin of error (MAE) of **₹99,796.98 (approx. ₦1.84M)**.

Furthermore, an interactive **Jupyter Dashboard Widget** was engineered to allow instant real-time valuation in both Indian Rupees (INR) and localized Nigerian Naira (NGN).

---

## 2. Dataset Architecture & Preprocessing

### 2.1 Raw Data Structure
The raw dataset comprised 15,411 rows and 14 columns:
* **Categorical Features:** `car_name`, `brand`, `model`, `seller_type`, `fuel_type`, `transmission_type`.
* **Numerical Features:** `vehicle_age`, `km_driven`, `mileage`, `engine`, `max_power`, `seats`.
* **Target Variable ($y$):** `selling_price`.

### 2.2 Data Quality Audit & Outlier Removal
During data inspection via `df.info()` and descriptive statistics, an extreme anomaly was flagged at **Row 15409 (Mahindra XUV500)**:
* **Vehicle Age:** 5 years ($\approx 1,825$ days)
* **Kilometers Driven:** **3,800,000 km** ($\approx 2,082$ km driven per day, non-stop).

**Resolution:** An outlier filtering threshold was established at `km_driven <= 1,000,000`. This eliminated two physically impossible data entry errors, preventing skewness in loss functions during optimization.

### 2.3 Feature Preprocessing & One-Hot Encoding
Machine learning algorithms require numerical input matrices. Non-numeric columns (`seller_type`, `fuel_type`, `transmission_type`) were encoded using **One-Hot Encoding** (`pd.get_dummies(X, drop_first=True)`). High-cardinality metadata (`car_name`, `model`) were dropped to prevent curse-of-dimensionality overfitting.

* **Original Feature Space:** 13 variables
* **Encoded Feature Space ($X$):** 44 features
* **Total Cleaned Observations:** 15,409 rows

---

## 3. Exploratory Data Analysis (EDA) Key Insights

1. **Price Skewness:** The `selling_price` distribution exhibits a right-skewed log-normal shape. The vast majority of transaction volumes occur under ₹1,000,000, with a sparse tail of high-value luxury models stretching up to ₹40,000,000.
2. **Fuel Type Dynamics:** Electric and Diesel variants exhibit higher median prices compared to Petrol, LPG, and CNG models.
3. **Correlation Matrix Findings:**
   * **`max_power` vs `selling_price`:** **$+0.75$** (Strongest positive driver of value).
   * **`engine` size vs `selling_price`:** **$+0.59$** (Moderate-strong positive correlation).
   * **`mileage` vs `engine` size:** **$-0.63$** (Strong negative inverse relationship; larger engines yield lower fuel efficiency).
   * **`mileage` vs `selling_price`:** **$-0.31$** (Negative correlation; fuel economy is prioritized in budget segments rather than luxury segments).

---

## 4. Machine Learning Methodology & Conceptual Masterclass

### 4.1 Comparative Model Breakdown

#### A. Linear Regression (The Parametric Straight-Line Baseline)
* **Concept:** Assumes a direct, additive linear relationship between independent features ($X$) and the dependent target ($y$):
  $$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon$$
* **Strength:** Fast, highly interpretable, low computational footprint.
* **Weakness:** Cannot capture non-linear relationships or complex interaction effects (e.g., luxury brand depreciation rates vs. economy brand depreciation rates).

#### B. Random Forest Regressor (The Ensemble Decision Tree Committee)
* **Concept:** Construct an ensemble of $N$ decision trees (100 trees in our implementation) trained on bootstrap samples of the data (Bagging). Each tree splits data based on feature conditions, and the final output is the unweighted average prediction across all 100 trees:
  $$\hat{y} = \frac{1}{N} \sum_{i=1}^{N} T_i(x)$$
* **Strength:** Excellent at handling complex non-linear curves, categorical features, and non-monotonic relationships.

### 4.2 Deep Dive Q&A: Conceptual Clarifications

#### Q1: How do we know if data is linear or requires a Random Forest?
**Answer:** We perform scatter plot visualizations ($y_{actual}$ vs $y_{predicted}$) and examine correlation matrices. Linear relationships form diagonal bands; non-linear realities appear as clusters, step-functions, or curves. Furthermore, empirical benchmarking—training a simple Linear Regression model first as a baseline—provides the definitive benchmark. If Random Forest outperforms it significantly, the data contains inherent non-linear complexities.

#### Q2: When do we use Linear Regression vs. Random Forest in production?
* **Use Linear Regression when:** Regulatory compliance requires complete model transparency (e.g., credit scoring under strict banking mandates), computational resources are constrained, or the problem domain is demonstrably linear.
* **Use Random Forest when:** Predictive accuracy is the primary objective, feature interactions are multi-dimensional, and dataset features consist of mixed types (categorical + continuous).

#### Q3: In Train-Test Split, is 80/20 mandatory? What about 70/30?
**Answer:** No split ratio is mathematically compulsory. 80/20, 70/30, and 75/25 are standard empirical choices. In `scikit-learn`, `test_size` accepts a float decimal between 0.0 and 1.0 representing the proportion of test samples. Passing `test_size=0.3` allocates 30% to testing and 70% to training. Passing an integer like `30` allocates exactly 30 individual samples to testing.

---

## 5. Model Evaluation & Results

Both models were evaluated on identical, unseen test datasets ($N = 3,082$ vehicles, 20% split).

| Evaluation Metric | Linear Regression Baseline | Random Forest Regressor | Performance Delta / Improvement |
| :--- | :--- | :--- | :--- |
| **Mean Absolute Error (MAE)** | ₹212,123.08 | **₹99,796.98** | **52.95% Error Reduction** 📉 |
| **Root Mean Squared Error (RMSE)** | ₹427,863.91 | **₹211,364.70** | **50.60% Error Reduction** 📉 |
| **$R^2$ Score (Variance Explained)** | 0.7473 (74.73%) | **0.9383 (93.83%)** | **+19.10% Accuracy Gain** 🚀 |

### 5.1 Feature Importance Findings
Extraction of tree Gini impurity reduction scores revealed the top 5 drivers of used car value:
1. **`max_power` (BHP):** Contributes over **65%** of relative predictive power.
2. **`vehicle_age`:** Second strongest factor (depreciation decay).
3. **`mileage`:** Fuel efficiency factor.
4. **`km_driven`:** Total engine wear usage.
5. **Luxury Brand Identifiers:** Brands like *Ferrari, Land Rover, Mercedes-Benz, Rolls-Royce* act as heavy step-up multipliers.

---

## 6. Interactive Dashboard & Deployment

To translate model output into business utility, a native **Jupyter Dashboard Widget** (`ipywidgets`) was built:
* **Inputs:** Sliders for `Year` (age conversion) and `Seats`; numeric text boxes for `KM Driven`, `Mileage`, `Engine (CC)`, `Max Power`; dropdowns for `Fuel Type`, `Seller Type`, `Transmission`.
* **Backend:** Serialized model loading (`pickle.load()`), dynamic one-hot input matrix construction matching training schema `(1, 44)`.
* **Output:** Instant valuation card displaying price in **INR (₹)** and real-time conversion to **NGN (₦)** at current exchange benchmarks.

---

## 7. Strategic Recommendations for Business Implementation

1. **Fintech Asset Financing (e.g., Kuda Bank):** Integrate the Random Forest pipeline via API to automatically evaluate collateral risk before approving auto loans.
2. **Automated Trade-in Valuation:** Deploy the interactive widget logic onto e-commerce landing pages to give sellers instant transparent valuation quotes, increasing user conversion rates.
3. **Inventory Acquisition Auditing:** Flag cars priced $\pm 20\%$ away from model predictions for manual review by human automotive appraisers to catch fraud or mispricing.

---
*Report compiled for the Oasis Infobyte Data Science Fellowship (OIBSIP) Task 3 Portfolio Repository.*