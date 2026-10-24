# Iris Flower Classification Project

An exploratory data analysis (EDA) and classification project using the classic **Iris Dataset**. This repository contains scripts and analysis documentation to inspect feature distributions, data hygiene, inter-species variations, and baseline classification readiness.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset Summary](#dataset-summary)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Requirements & Installation](#requirements--installation)
- [Usage Instructions](#usage-instructions)
- [Key Findings & Results Summary](#key-findings--results-summary)
- [License](#license)

---

## Project Overview

The primary objective of this project is to analyze the structural integrity and statistical properties of the Iris dataset and demonstrate machine learning classification workflows. Using physical measurements of flower sepals and petals, the project categorizes iris samples into one of three species:
* *Iris setosa*
* *Iris versicolor*
* *Iris virginica*

---

## Dataset Summary

The dataset contains 150 instances, evenly distributed across three species (50 instances per species). It includes 4 continuous numerical feature columns and categorical target mappings.

* **Total Samples:** 150
* **Missing Values:** None (0 null entries)
* **Target Classes:** 3 balanced classes

### Feature Specifications

| Feature Name | Type | Range (Min - Max) | Mean $\pm$ Std Dev |
| :--- | :--- | :--- | :--- |
| `sepal length (cm)` | Continuous (`float64`) | $4.30 - 7.90\text{ cm}$ | $5.84 \pm 0.83\text{ cm}$ |
| `sepal width (cm)` | Continuous (`float64`) | $2.00 - 4.40\text{ cm}$ | $3.06 \pm 0.44\text{ cm}$ |
| `petal length (cm)` | Continuous (`float64`) | $1.00 - 6.90\text{ cm}$ | $3.76 \pm 1.77\text{ cm}$ |
| `petal width (cm)` | Continuous (`float64`) | $0.10 - 2.50\text{ cm}$ | $1.20 \pm 0.76\text{ cm}$ |

---

## Key Features

- **Data Quality Audit:** Null-value checks, duplicate detection, and standard statistical summaries.
- **Exploratory Visualizations:** Distribution plots, correlation heatmaps, and multi-variable pair plots.
- **Data Documentation:** Comprehensive dataset breakdown and actionable recommendations for modeling.

---

## Requirements & Installation

### Prerequisites
* **Python Version:** Python 3.9 or higher
* **Environment:** Jupyter Notebook, JupyterLab, or VS Code Interactive

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/iris-classification.git
   cd iris-classification
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

---

## Usage Instructions

1. **Launch Jupyter Environment:**
   ```bash
   jupyter notebook
   ```
2. Open `iris_eda.ipynb` (or execute the standalone analysis script).
3. Run all cells to generate analysis summaries, correlation matrices, and distribution visualizations.

---

## Key Findings & Results Summary

1. **Linear Separability:** *Iris setosa* is completely linearly separable from *versicolor* and *virginica* based on petal length and petal width alone.
2. **Feature Importance:** Petal dimensions (`petal length` and `petal width`) possess significantly higher variance ($\sigma = 1.77$ and $\sigma = 0.76$ respectively) and predictive capability than sepal dimensions.
3. **Correlation:** A strong positive correlation exists between `petal length` and `petal width` ($r > 0.95$).

---

## License

This project is open-source and available under the [MIT License](LICENSE).