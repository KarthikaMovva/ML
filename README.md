# 🥗 My_Nutritionist

An AI-powered Nutrition Recommendation System that predicts personalized daily nutritional requirements using Machine Learning and recommends healthy foods based on the predicted nutrition profile, health conditions, dietary preferences, and allergies.

---

# 🚀 Features

- Predicts personalized daily nutrition targets
- Recommends foods based on nutritional similarity
- Supports multiple health conditions:
  - Healthy
  - Diabetes
  - Hypertension
  - Heart Disease
  - Obesity
- Supports dietary preferences
  - Vegetarian
  - Non-Vegetarian
- Supports allergy filtering
  - Nut Allergy
  - Dairy Allergy
  - Seafood Allergy
- Automatic BMI calculation
- FastAPI REST API
- React + Tailwind CSS frontend
- Scikit-Learn Multi-output Regression Model


---

# 🏗 Project Architecture

```
                React + Tailwind UI
                        │
                        │ REST API
                        ▼
                  FastAPI Backend
                        │
        ┌───────────────┴────────────────┐
        │                                │
        ▼                                ▼
 Nutrition Prediction Model      Recommendation Engine
        │                                │
        ▼                                ▼
 Predicted Nutrition Targets     Food Filtering & Ranking
        │                                │
        └───────────────┬────────────────┘
                        ▼
              Final Food Recommendations
```

---

# 🧠 Machine Learning Pipeline

```
Synthetic Patient Dataset
            │
            ▼
Feature Engineering
            │
            ▼
Preprocessing Pipeline
(ColumnTransformer)
            │
            ▼
RandomForestRegressor
(MultiOutput Regression)
            │
            ▼
Predict Nutrition Targets
```

---

# 🍽 Recommendation Engine Pipeline

```
Patient Information
        │
        ▼
Predict Nutrition Targets
        │
        ▼
Apply Health Rules

Diabetes
Hypertension
Heart Disease
Obesity

        │
        ▼
Diet Filter

Vegetarian
Non Vegetarian

        │
        ▼
Allergy Filter

Nut
Dairy
Seafood

        │
        ▼
Remove Low Quality Foods

        │
        ▼
Cosine Similarity

        │
        ▼
Nutrition Distance Score

        │
        ▼
Final Ranking

        │
        ▼
Top Food Recommendations
```

# 🛠 Tech Stack

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib

---

## Backend

- FastAPI
- Uvicorn
- Pydantic

---

## Frontend

- React
- Tailwind CSS
- Axios

---

# 📊 Dataset

## Patient Dataset

A synthetic dataset of **20,000 patient records** was generated with:

- Age
- Gender
- Height
- Weight
- BMI
- Activity Level
- Health Condition
- Diet Preference
- Allergy

The dataset was enriched with nutrition targets using rule-based calculations.

---

## Food Dataset

Contains **2395 food items** with nutritional values including:

- Calories
- Protein
- Carbohydrates
- Fat
- Dietary Fiber
- Sugar
- Sodium
- Vitamins
- Minerals

---

# 🤖 Model Training

The nutrition prediction model uses:

```
ColumnTransformer
        │
        ▼
OneHotEncoder
StandardScaler
        │
        ▼
RandomForestRegressor
```

The model predicts:

- Calories
- Protein
- Carbohydrates
- Fat
- Fiber
- Maximum Sugar
- Maximum Sodium


# 🧩 Recommendation Strategy

The recommendation engine does **not** directly predict foods.

Instead it follows a production-style architecture:

1. Predict patient nutrition targets
2. Filter foods using medical rules
3. Filter by diet preference
4. Filter allergens
5. Remove low-quality foods
6. Calculate cosine similarity
7. Compute nutrition distance
8. Rank foods using a weighted score
9. Return the Top-N recommendations

# 📡 API Endpoints

## Home

```
GET /
```

---

## Predict Nutrition

```
POST /predict
```

Returns predicted nutrition targets.

---

## Recommend Foods

```
POST /recommend
```

Returns:

- Nutrition targets
- Top food recommendations

---

# 🖥 User Interface

The application allows users to:

- Enter patient information
- Automatically calculate BMI
- Predict nutrition requirements
- Receive personalized food recommendations
- View recommended nutrients and foods

---

# 🔮 Future Improvements

- Meal planning (Breakfast, Lunch, Dinner)
- Weekly diet planner
- Grocery list generation
- AI chatbot nutrition assistant
- LLM-powered explanation for recommendations
- RAG integration using nutrition guidelines
- User authentication
- Nutrition history dashboard
- Docker deployment
- CI/CD pipeline
- Cloud deployment (AWS/Azure)

---

# 🎯 Learning Outcomes

Through this project I learned:

- End-to-end Machine Learning workflow
- Feature Engineering
- Multi-output Regression
- FastAPI development
- React integration
- Recommendation Systems
- Cosine Similarity
- Model Deployment
- REST API development
- Production-style project architecture

---

