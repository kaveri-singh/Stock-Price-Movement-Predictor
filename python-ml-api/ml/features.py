import pandas as pd
import numpy as np

def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Basic features
    df['return'] = df['Close'].pct_change()
    df['volatility'] = df['Close'].rolling(window=5).std()
    
    # Moving averages
    df['ma5'] = df['Close'].rolling(window=5).mean()
    df['ma10'] = df['Close'].rolling(window=10).mean()
    
    # Volume trend
    df['volume_change'] = df['Volume'].pct_change()
    
    # Target: 1 if next day close is higher, else 0
    df['target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    
    df.dropna(inplace=True)
    return df
