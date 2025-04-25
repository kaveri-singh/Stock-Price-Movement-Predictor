# ml/model.py
import pandas as pd
import joblib

MODEL_PATH = "ml/model/stock_movement_model.pkl"
SCALER_PATH = "ml/model/scaler.pkl"

# Load the model
def load_model():
    model = joblib.load(MODEL_PATH)
    return model

# Load the scaler
def load_scaler():
    scaler = joblib.load(SCALER_PATH)
    return scaler

# Predict stock movement
def predict_stock_movement(data: pd.DataFrame):
    model = load_model()
    scaler = load_scaler()

    # Scale the input data
    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)
    confidence = model.predict_proba(data_scaled).max(axis=1)[0]

    return {"prediction": "Up" if prediction[0] == 1 else "Down", "confidence": confidence}
