import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "60d", interval: str = "1d") -> pd.DataFrame:
    df = yf.download(ticker, period=period, interval=interval, auto_adjust=True)
    
    if df.empty:
        raise ValueError("Failed to fetch stock data.")
    
    df.dropna(inplace=True)
    return df
