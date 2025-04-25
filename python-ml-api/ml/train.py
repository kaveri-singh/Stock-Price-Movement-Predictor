# ml/train_model.py
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Create model directory if it doesn't exist
os.makedirs("ml/model", exist_ok=True)

def fetch_stock_data(ticker: str, period="180d", interval="1d") -> pd.DataFrame:
    df = yf.download(ticker, period=period, interval=interval)
    df.dropna(inplace=True)
    return df

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df['Price_Change'] = df['Close'].pct_change()
    df['Target'] = np.where(df['Price_Change'].shift(-1) > 0, 1, 0)
    df.dropna(inplace=True)
    return df

def train_model(ticker="INFY.NS"):
    df = fetch_stock_data(ticker)
    df = create_features(df)

    X = df[["Open", "High", "Low", "Close", "Volume"]]
    y = df["Target"]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Model training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Accuracy
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Model accuracy: {acc:.2f}")

    # Save model and scaler
    joblib.dump(model, "ml/model/stock_movement_model.pkl")
    joblib.dump(scaler, "ml/model/scaler.pkl")

if __name__ == "__main__":
    train_model()
