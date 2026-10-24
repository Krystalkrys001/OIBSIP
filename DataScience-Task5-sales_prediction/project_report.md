# Comprehensive Project Report: Sales Prediction & Marketing ROI Optimization

**Program:** Oasis Infobyte Data Science Internship (OIBSIP)  
**Task:** Task 5 – Sales Prediction Using Python  
**Dataset:** Advertising.csv (200 records)  

---

## 1. Executive Summary

This report presents a multiple linear regression analysis designed to quantify the relationship between advertising investments across **TV**, **Radio**, and **Newspaper** channels and resulting **Product Sales**.

Utilizing Python, pandas, and scikit-learn, an Ordinary Least Squares (OLS) model was built on an 80/20 train-test split (160 training rows, 40 test rows). The model achieved an **$R^2$ score of 0.8994** and a **Root Mean Squared Error (RMSE) of 1.7816**. 

Feature coefficient analysis demonstrates that **Radio advertising delivers the highest marginal ROI ($0.1892$)**, **TV drives baseline sales volume ($0.0447$)**, and **Newspaper advertising yields virtually no marginal sales return ($0.0028$)**.

---

## 2. Dataset Architecture & Quality Audit

The dataset consists of 200 observations representing sales figures across different media budget combinations.

### Data Audit Findings:
1. **Redundant Column Removal:** The initial CSV file contained an un-named index column (Unnamed: 0) ranging from 1 to 200, which was removed to prevent bias in regression weights.
2. **Missing Value Audit:** All 200 records contained complete numerical values across all four variables.
3. **Data Types:** All features represent continuous float values.

### Summary Statistics

```text
       TV        Radio      Newspaper    Sales
mean   147.0425   23.2640    30.5540     14.0225
std     85.8542   14.8468    21.7786      5.2175
min      0.7000    0.0000     0.3000      1.6000
25%     74.3750    9.9750    12.7500     10.3750
50%    149.7500   22.9000    25.7500     12.9000
75%    218.8250   36.5250    45.1000     17.4000
max    296.4000   49.6000   114.0000     27.0000
```

---

## 3. Exploratory Data Analysis & Feature Interaction

To test the assumption of linearity required for regression models, pairwise scatter plots and a correlation matrix were computed.

### Correlation Heatmap Values:
* **TV $\rightarrow$ Sales:** $r = 0.782$ (Strong linear trend)
* **Radio $\rightarrow$ Sales:** $r = 0.576$ (Moderate-strong linear trend)
* **Newspaper $\rightarrow$ Sales:** $r = 0.228$ (Weak relationship)
* **TV $\rightarrow$ Radio:** $r = 0.055$ (Independent)
* **TV $\rightarrow$ Newspaper:** $r = 0.057$ (Independent)
* **Radio $\rightarrow$ Newspaper:** $r = 0.354$ (Low correlation)

**Key Finding:** Because predictor variables display minimal inter-correlation, the dataset is free from severe **multicollinearity**, satisfying a key assumption of linear regression.

---

## 4. Regression Modeling & Empirical Results

The dataset was divided into training ($N=160$) and test ($N=40$) sets using random_state=42.

### Empirical Results Summary:
* **Intercept ($\beta_0$):** 2.9791 (Baseline sales without media spend)
* **TV Coefficient ($\beta_1$):** 0.044730
* **Radio Coefficient ($\beta_2$):** 0.189195
* **Newspaper Coefficient ($\beta_3$):** 0.002761
* **$R^2$ Score:** 0.8994
* **RMSE:** 1.7816

### Mathematical Model Equation:

$$\hat{Y}_{\text{Sales}} = 2.9791 + 0.044730(\text{TV}) + 0.189195(\text{Radio}) + 0.002761(\text{Newspaper}) + #$$

---

## 5. Strategic Business Recommendations (Marketing Attribution)

1. **Terminate Newspaper Capital Allocation:** The structural coefficient for Newspaper (\(0.0028\)) indicates that investing $10,000 yields a negligible <28 units in sales. Newspaper ad spend should be aggressively cut to zero..
2. **Maximize Radio Efficiency (Top ROI Pick):** Radio delivers your highest marginal efficiency, yielding an incremental 189.2 units per $1,000 spent (\(\beta_2 = 0.1892\)). This is your prime growth accelerator.
3. **Anchor TV for High-Volume Reach:** • While Radio is more efficient dollar-for-dollar, TV maintains the strongest linear correlation (\(r = 0.782\)) to top-line volume. Maintain TV as your baseline foundational engine.

---

## 6. Model Diagnostics & Error Analysis

Residuals ($\epsilon_i = y_i - \hat{y}_i$) were plotted against predicted sales values to verify regression assumptions:
* **Zero Mean:** Errors are centered around zero ($y = 0$).
* **Variance Distribution:** Residuals lie primarily within $[-3.5, +2.5]$, indicating bounded, predictable error ranges.
* **Non-Linearity Note:** A slight parabolic curvature in the residual scatter highlights potential synergy between TV and Radio (interaction effects), which can be explored in future modeling iterations using polynomial features.

---

## 7. Conclusion

The developed Ordinary Least Squares regression model provides an **$89.94\%$ explanation of sales variance** with a low error margin ($1.7816$). It delivers both actionable marketing budget recommendations and verified predictive reliability for business planning.
