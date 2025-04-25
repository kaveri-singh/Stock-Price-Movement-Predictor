import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ml.model import predict_stock_movement  # Importing your ML function

# Initialize the FastAPI app
app = FastAPI()

# Define the input data model
class StockRequest(BaseModel):
    ticker: str

# Define the prediction response model
class StockPredictionResponse(BaseModel):
    prediction: str
    confidence: float

@app.post("/predict", response_model=StockPredictionResponse)
async def predict_stock(request: StockRequest):
    try:
        # Call the ML function to predict stock movement
        result = predict_stock_movement(request.ticker)
        
        # If there's an error in the prediction (empty data, etc.)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])

        # Return the prediction and confidence
        return StockPredictionResponse(
            prediction=result["prediction"],
            confidence=result["confidence"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# If needed, add more routes for additional functionality like training the model, etc.
