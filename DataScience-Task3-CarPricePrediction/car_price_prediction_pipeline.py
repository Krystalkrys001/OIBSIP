"""
================================================================================
Oasis Infobyte Data Science Fellowship (OIBSIP) - Task 3
Project: Car Price Prediction with Machine Learning
Author: Chukwuma Obinna Ulasi
Location: Lagos, Nigeria
================================================================================
Description:
    An end-to-end Machine Learning pipeline that predicts used car prices using
    the Cardekho dataset. Demonstrates data cleaning, exploratory data analysis,
    One-Hot Encoding, train-test splitting, model training (Linear Regression vs.
    Random Forest Regressor), model persistence via pickle, and an interactive 
    Jupyter UI widget for real-time valuation in INR and NGN.
================================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import ipywidgets as widgets
from IPython.display import display, HTML

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==============================================================================
# BLOCK 1: DATA LOADING & INITIAL INSPECTION
# ==============================================================================
def load_data(filepath: str) -> pd.DataFrame:
    print("[INFO] Loading dataset from path:", filepath)
    df = pd.read_csv(filepath)
    print(f"[INFO] Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.\n")
    return df

# ==============================================================================
# BLOCK 2: DATA CLEANING & PREPROCESSING
# ==============================================================================
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print("[INFO] Starting Data Cleaning Pipeline...")
    
    # 1. Drop redundant index columns if present
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
        print(" -> Removed redundant 'Unnamed: 0' index column.")
        
    # 2. Inspect categorical unique values
    print(" -> Unique Seller Types:", df['seller_type'].unique())
    print(" -> Unique Fuel Types:", df['fuel_type'].unique())
    print(" -> Unique Transmission Types:", df['transmission_type'].unique())
    
    # 3. Handle extreme outliers in km_driven (e.g., impossible > 1,000,000 km entries)
    initial_rows = len(df)
    df = df[df['km_driven'] <= 1000000]
    removed_rows = initial_rows - len(df)
    print(f" -> Outlier Filtering Complete: Removed {removed_rows} unrealistic rows (km_driven > 1,000,000 km).")
    
    return df

# ==============================================================================
# BLOCK 3: EXPLORATORY DATA ANALYSIS (EDA) & VISUALIZATION
# ==============================================================================
def run_eda(df: pd.DataFrame):
    print("\n[INFO] Generating Exploratory Data Analysis Visualizations...")
    sns.set_theme(style="whitegrid")
    
    # 1. Target Variable Distribution
    plt.figure(figsize=(10, 5))
    sns.histplot(df['selling_price'], kde=True, color='blue', bins=50)
    plt.title('Distribution of Car Selling Prices')
    plt.xlabel('Selling Price')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

    # 2. Price vs. Fuel Type Boxplot
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='fuel_type', y='selling_price', data=df, palette='Set2')
    plt.title('Selling Price vs. Fuel Type')
    plt.xlabel('Fuel Type')
    plt.ylabel('Selling Price')
    plt.tight_layout()
    plt.show()

    # 3. Correlation Heatmap for Numerical Features
    plt.figure(figsize=(8, 6))
    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# BLOCK 4: FEATURE ENGINEERING & DATA SPLITTING
# ==============================================================================
def prepare_features(df: pd.DataFrame):
    print("\n[INFO] Preparing Features & Target for Model Training...")
    
    # Drop non-predictive/high-cardinality metadata and target column
    X = df.drop(columns=['car_name', 'model', 'selling_price'])
    y = df['selling_price']
    
    # One-Hot Encoding for categorical text columns
    X = pd.get_dummies(X, drop_first=True)
    
    print(f" -> Feature Matrix (X) Shape: {X.shape}")
    print(f" -> Target Vector (y) Shape: {y.shape}")
    
    # 80/20 Train-Test Split (test_size=0.2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f" -> Training set size: {X_train.shape[0]} samples")
    print(f" -> Testing set size: {X_test.shape[0]} samples")
    
    return X, y, X_train, X_test, y_train, y_test

# ==============================================================================
# BLOCK 5: MODEL TRAINING & EVALUATION
# ==============================================================================
def evaluate_model(true_values, predictions, model_name: str):
    mae = mean_absolute_error(true_values, predictions)
    rmse = np.sqrt(mean_squared_error(true_values, predictions))
    r2 = r2_score(true_values, predictions)
    
    print(f"--- {model_name.upper()} PERFORMANCE ---")
    print(f"MAE (Mean Absolute Error)     : ₹{mae:,.2f}")
    print(f"RMSE (Root Mean Squared Error): ₹{rmse:,.2f}")
    print(f"R² Score (Accuracy Metric)    : {r2:.4f}\n")
    return mae, rmse, r2

def train_and_evaluate(X, X_train, X_test, y_train, y_test):
    print("\n[INFO] Training Machine Learning Models...")
    
    # 1. Linear Regression Baseline
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)
    evaluate_model(y_test, lr_pred, "Linear Regression")

    # 2. Random Forest Regressor
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    evaluate_model(y_test, rf_pred, "Random Forest Regressor")

    # 3. Model Comparison Plot
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)
    axes[0].scatter(y_test, lr_pred, color='crimson', alpha=0.5)
    axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    axes[0].set_title('Linear Regression: Actual vs Predicted')
    axes[0].set_xlabel('Actual Selling Price')
    axes[0].set_ylabel('Predicted Selling Price')

    axes[1].scatter(y_test, rf_pred, color='teal', alpha=0.5)
    axes[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    axes[1].set_title('Random Forest: Actual vs Predicted')
    axes[1].set_xlabel('Actual Selling Price')

    plt.tight_layout()
    plt.show()

    # 4. Feature Importance Analysis
    feature_importances = pd.Series(rf_model.feature_importances_, index=X.columns)
    plt.figure(figsize=(10, 6))
    feature_importances.nlargest(10).plot(kind='barh', color='teal')
    plt.title('Top 10 Most Important Features Driving Car Prices')
    plt.xlabel('Relative Importance')
    plt.ylabel('Feature')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

    # Save trained model and feature structure
    with open('car_price_model.pkl', 'wb') as f:
        pickle.dump(rf_model, f)
    with open('model_columns.pkl', 'wb') as f:
        pickle.dump(X.columns.tolist(), f)
    print("[INFO] Model and feature schema persisted to disk ('car_price_model.pkl', 'model_columns.pkl').")

    return rf_model

# ==============================================================================
# BLOCK 6: INTERACTIVE UI DASHBOARD (IPYWIDGETS)
# ==============================================================================
def launch_interactive_dashboard():
    try:
        with open('car_price_model.pkl', 'rb') as model_file:
            rf_model = pickle.load(model_file)
        with open('model_columns.pkl', 'rb') as columns_file:
            saved_columns = pickle.load(columns_file)
    except FileNotFoundError:
        print("[ERROR] Model files not found. Please run model training first.")
        return

    style = {'description_width': 'initial'}
    year_input = widgets.IntSlider(value=2018, min=1990, max=2026, description="Year:", style=style)
    km_input = widgets.IntText(value=50000, description="KM Driven:", style=style)
    mileage_input = widgets.FloatText(value=18.5, description="Mileage (km/L):", style=style)
    engine_input = widgets.IntText(value=1200, description="Engine (CC):", style=style)
    power_input = widgets.FloatText(value=85.0, description="Max Power (BHP):", style=style)
    seats_input = widgets.SelectionSlider(options=list(range(2, 11)), value=5, description="Seats:", style=style)

    fuel_input = widgets.Dropdown(options=["Petrol", "Diesel", "CNG", "LPG"], value="Petrol", description="Fuel Type:", style=style)
    seller_input = widgets.Dropdown(options=["Individual", "Dealer", "Trustmark Dealer"], value="Individual", description="Seller Type:", style=style)
    trans_input = widgets.Dropdown(options=["Manual", "Automatic"], value="Manual", description="Transmission:", style=style)

    button = widgets.Button(description="Calculate Estimated Value", button_style='success', layout=widgets.Layout(width='50%'))
    output = widgets.Output()

    def on_button_clicked(b):
        with output:
            output.clear_output()
            vehicle_age = 2026 - year_input.value
            input_data = pd.DataFrame(0, index=[0], columns=saved_columns)
            
            if 'vehicle_age' in input_data.columns: input_data['vehicle_age'] = vehicle_age
            if 'km_driven' in input_data.columns: input_data['km_driven'] = km_input.value
            if 'mileage' in input_data.columns: input_data['mileage'] = mileage_input.value
            if 'engine' in input_data.columns: input_data['engine'] = engine_input.value
            if 'max_power' in input_data.columns: input_data['max_power'] = power_input.value
            if 'seats' in input_data.columns: input_data['seats'] = seats_input.value

            for col in input_data.columns:
                if f"fuel_type_{fuel_input.value}" in col: input_data[col] = 1
                if f"seller_type_{seller_input.value}" in col: input_data[col] = 1
                if f"transmission_type_{trans_input.value}" in col: input_data[col] = 1

            pred_rupees = rf_model.predict(input_data)[0]
            pred_naira = pred_rupees * 18.50  # Real-time indicative FX conversion
            
            display(HTML(f"""
            <div style="padding:15px; background-color:#e1f5fe; border-radius:5px; border-left: 5px solid #0288d1; margin-top:10px;">
                <h4 style="margin:0; color:#01579b;">🚗 Valuation Complete!</h4>
                <p style="margin:5px 0 0 0; font-size:16px;"><b>Estimated Market Value (INR):</b> ₹{pred_rupees:,.2f}</p>
                <p style="margin:5px 0 0 0; font-size:18px; color:#2e7d32;"><b>Estimated Nigerian Market Value (NGN):</b> ₦{pred_naira:,.2f}</p>
            </div>
            """))

    button.on_click(on_button_clicked)

    st_ui = widgets.VBox([
        widgets.HTML("<h2>🚗 Used Car Price Predictor Dashboard</h2>"),
        widgets.TwoByTwoLayout(top_left=year_input, top_right=engine_input, bottom_left=km_input, bottom_right=power_input),
        widgets.TwoByTwoLayout(top_left=mileage_input, top_right=fuel_input, bottom_left=seats_input, bottom_right=seller_input),
        widgets.HBox([trans_input]), widgets.HTML("<br>"), button, output
    ])
    display(st_ui)

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    df_raw = load_data('cardekho_dataset.csv')
    df_clean = clean_data(df_raw)
    run_eda(df_clean)
    X, y, X_train, X_test, y_train, y_test = prepare_features(df_clean)
    rf_model = train_and_evaluate(X, X_train, X_test, y_train, y_test)
    launch_interactive_dashboard()