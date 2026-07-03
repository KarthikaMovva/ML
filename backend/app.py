from fastapi import FastAPI
import pandas as pd
import joblib
from predictor import predict_nutrition
from schemas import PatientRequest

app = FastAPI(                                            #First API with swagger UI
    title="AI Nutrition Recommendation API",
    version="1.0.0"
)

model = joblib.load("models/nutrition_model.pkl")      #Load the nutrition model

scaler = joblib.load("models/food_scaler.pkl")          #Load the food scaler

recommendation_df = pd.read_csv("data/processed/food_nutrition.csv")   #load the food dataset

@app.get("/")                       #created first endpoint
def home():
    return {
        "message": "AI Nutrition Recommendation API is running!"
    }

@app.post("/predict")
def predict(patient: PatientRequest):

    nutrition = predict_nutrition(
        model,
        patient.model_dump()
    )

    return nutrition