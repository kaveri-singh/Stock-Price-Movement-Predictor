# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from ml.model import predict_stock_movement
import yfinance as yf

app = FastAPI()

class StockRequest(BaseModel):
    ticker: str

@app.post("/predict")
def predict(request: StockRequest):
    # 1. Download recent data for the stock
    df = yf.download(request.ticker, period="7d", interval="1d")
    if df.empty or len(df) < 2:
        return {"error": "Not enough data to make prediction."}
    
    # 2. Preprocess the data
    df['Price_Change'] = df['Close'].pct_change()
    df['Target'] = (df['Price_Change'].shift(-1) > 0).astype(int)
    df.dropna(inplace=True)

    # 3. Use only latest row's features
    latest = df[["Open", "High", "Low", "Close", "Volume"]].tail(1)

    # 4. Predict using ML model
    result = predict_stock_movement(latest)
    return result
