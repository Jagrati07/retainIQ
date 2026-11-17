import pandas as pd
def clean_data(df):
    df = df.copy()
    # Convert TotalCharges into numbers
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    # Fill missing TotalCharges for customers with zero tenure
    df["TotalCharges"] = df["TotalCharges"].fillna(0)
    # Convert Churn into 0 and 1
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    return df
