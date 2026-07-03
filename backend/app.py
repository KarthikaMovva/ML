from fastapi import FastAPI
import pandas as pd
import joblib
from predictor import predict_nutrition
from schemas import PatientRequest
from recommender import recommend_foods
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(                                            #First API with swagger UI
    title="AI Nutrition Recommendation API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("models/nutrition_model.pkl")      #Load the nutrition model

scaler = joblib.load("models/food_scaler.pkl")          #Load the food scaler

recommendation_df = pd.read_csv("data/processed/food_nutrition.csv")   #load the food dataset

@app.get("/")                       #created first endpoint
def home():
    return {
        "message": "AI Nutrition Recommendation API is running!"
    }

@app.post("/predict")                               #This endpoint predicts the target nutrition requirements
def predict(patient: PatientRequest):

    nutrition = predict_nutrition(
        model,
        patient.model_dump()
    )

    return nutrition

@app.post("/recommend")                      #This end point Return prediction of target nutritional requirements + recommendations of foods based on target requirements together
def recommend(patient: PatientRequest):

    patient_df = patient.model_dump()

    nutrition = predict_nutrition(
        model,
        patient_df
    )

    recommendations = recommend_foods(
        patient_df,
        model,
        recommendation_df,
        scaler,
        top_n=5
    )

    return {
        "nutrition_targets": nutrition,
        "recommendations": recommendations.to_dict(orient="records")
    }