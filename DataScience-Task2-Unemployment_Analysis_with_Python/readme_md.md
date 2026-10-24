# Task 2: Unemployment Analysis with Python

## 📌 Project Overview
This project performs an **Exploratory Data Analysis (EDA)** on unemployment data across various regions and states in India. The study focuses on uncovering regional variations, temporal trends, and evaluating the macroeconomic shock caused by the **COVID-19 pandemic** on labor participation and employment rates in 2020.

---

## 🎯 Objectives
* Inspect, clean, and pre-process time-series regional unemployment data.
* Identify states/regions experiencing the highest average unemployment rates.
* Visualize timeline trends across major states to highlight lockdown-induced shocks.
* Evaluate correlations between unemployment rate, employment count, and labor force participation rate.
* Conduct a **Pre-COVID vs. Post-COVID** comparative analysis to quantify the pandemic's impact on labor market dynamics.

---

## 📊 Dataset Details
* **Dataset Name:** Unemployment_Rate_upto_11_2020.csv / Unemployment in India.csv
* **Source:** Kaggle
* **Records:** 267 entries across Indian states/regions (Monthly granularity, Jan 2020 – Oct 2020)
* **Key Attributes:**
  * Region: Name of the state/union territory.
  * Date: Date of monthly observation.
  * Estimated Unemployment Rate (%): Percentage of the unemployed labor force.
  * Estimated Employed: Total count of employed individuals.
  * Estimated Labour Participation Rate (%): Percentage of the working-age population participating in the labor force.
  * Region.1: Geographic zone (North, South, East, West, North East).

---

## 🛠 Tech Stack
* **Language:** Python 3.12+
* **Environment:** Jupyter Notebook / Anaconda
* **Libraries:**
  * pandas — Data manipulation, aggregation, and datetime processing.
  * numpy — Array operations and quantitative calculations.
  * matplotlib — Base plotting and line chart customization.
  * seaborn — Statistical visualizations, heatmaps, and bar charts.

---

## 🚀 Installation & Setup

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/your-username/unemployment-analysis-python.git
   cd unemployment-analysis-python
   ```

2. **Install Required Libraries:**
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. **Launch the Jupyter Notebook:**
   ```bash
   jupyter notebook unemployment_analysis.ipynb
   ```

---

## 📈 Key Features & Visual Insights

### 1. Data Cleaning & Inspection
* **Completeness:** 0 missing values across all 9 features ($267 \times 9$ dataset shape).
* **Type Conversion:** Successfully cast string date columns into standard Pandas `datetime64` types (`dayfirst=True`).

### 2. Regional Analysis (Top 10 Unemployed States)
* **Insight:** **Haryana** recorded the highest average unemployment rate ($\approx 27.48\%$), followed by **Tripura** ($\approx 25.06\%$), **Jharkhand** ($\approx 19.54\%$), and **Bihar** ($\approx 19.47\%$).

### 3. Time-Series Trends (Pandemic Surge)
* **Insight:** Tracking major states (*Maharashtra, Tamil Nadu, Uttar Pradesh*) over time highlights an extreme spike in unemployment in **April–May 2020**, coinciding with strict nationwide lockdowns. Tamil Nadu saw unemployment peak near **$50\%$** during May 2020 before recovering.

### 4. Correlation Matrix Heatmap
* **Insight:** Displays a negative correlation ($-0.25$) between the *Unemployment Rate* and *Estimated Employed* count, illustrating how sharp rises in unemployment directly depleted active wage earners.

### 5. Pre-COVID vs. Post-COVID Impact Analysis
* **Lockdown Threshold Date:** March 24, 2020
* **Quantitative Shift:**
  * **Mean Unemployment Rate:** Rose from **$9.23\%$** (Pre-COVID) to **$12.96\%$** (Post-COVID).
  * **Mean Employed Count:** Dropped from **$15.56 \text{ Million}$** to **$13.57 \text{ Million}$**.
  * **Labour Participation Rate:** Declined from **$44.40\%$** to **$41.02\%$**.

---

## 📜 Key Observations & Conclusion
1. **Macroeconomic Vulnerability:** The COVID-19 lockdown created a severe, immediate labor market shock across both urban and rural regions.
2. **State-Level Disparities:** Industrialized and heavily populated states showed varying recovery trajectories, with southern and northern states showing distinct recovery slopes post-June 2020.
3. **Policy Takeaway:** Future economic crisis interventions must target regions with high baseline unemployment and vulnerable informal labor segments.
