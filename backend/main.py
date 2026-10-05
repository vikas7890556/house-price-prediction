from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices using a trained Random Forest model",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# LOAD TRAINED MODEL
# ============================================================

model = joblib.load("house_price_model.pkl")


# ============================================================
# INPUT DATA MODEL
# ============================================================

class HouseData(BaseModel):

    bedrooms: int
    bathrooms: float
    sqft_living: float
    sqft_lot: float
    floors: float
    waterfront: int
    view: int
    condition: int
    grade: int
    sqft_above: float
    sqft_basement: float
    yr_built: int
    sqft_living15: float
    lat: float
    long: float
    zipcode: int


# ============================================================
# HOME ENDPOINT
# ============================================================

@app.get("/")
def home():

    return {
        "message": "House Price Prediction API is running!"
    }


# ============================================================
# MODEL INFO ENDPOINT
# ============================================================

@app.get("/model-info")
def model_info():

    return {
        "message": "House Price Prediction Model loaded successfully!"
    }


# ============================================================
# PREDICTION ENDPOINT
# ============================================================

@app.post("/predict")
def predict_price(house: HouseData):

    # Convert incoming data into a dictionary
    house_data = house.model_dump()

    # Convert dictionary into DataFrame
    house_df = pd.DataFrame([house_data])

    # Make prediction
    prediction = model.predict(house_df)

    # Return predicted price
    return {
        "predicted_price": round(float(prediction[0]), 2)
    }