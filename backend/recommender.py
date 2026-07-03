import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from predictor import predict_nutrition

NON_VEG = [
    "chicken",
    "beef",
    "fish",
    "pork",
    "lamb",
    "turkey",
    "duck",
    "shrimp",
    "crab",
    "mutton",
    "bacon"
]

ALLERGY_MAP = {

    "Nut Allergy":[
        "almond",
        "cashew",
        "walnut",
        "peanut"
    ],

    "Seafood Allergy":[
        "fish",
        "shrimp",
        "crab",
        "salmon",
        "tuna"
    ],

    "Dairy Allergy":[
        "milk",
        "cheese",
        "cream",
        "butter"
    ]
}

LOW_QUALITY_FOODS = [
    "chips",
    "fries",
    "burger",
    "pizza",
    "taco bell",
    "cola",
    "soft drink",
    "candy",
    "cookie",
    "cookies",
    "cake",
    "chocolate",
    "doughnut",
    "donut",
    "ice cream"
]

INVALID_FOODS = [
    "salt",
    "seasoning",
    "spices",
    "vinegar",
    "water",
    "gelatin",
    "food coloring",
    "baking powder",
    "yeast",
    "cornstarch",
    "shortening",
    "lard",
    "oil",
    "soy sauce",
    "extract"
]

MEAL_KEYWORDS = [
    "soup",
    "salad",
    "rice",
    "curry",
    "stew",
    "pasta",
    "sandwich",
    "beans",
    "vegetable"
]

def apply_health_rules(food_df, patient, nutrition):

    condition = patient["health_condition"]

    filtered = food_df.copy()

    if condition == "Diabetes":

        filtered = filtered[
            (filtered["sugars"] <= nutrition["sugars"] * 1.2) &
            (filtered["dietary_fiber"] >= nutrition["dietary_fiber"] * 0.3)
        ]

    elif condition == "Hypertension":

        filtered = filtered[
            filtered["sodium"] <= nutrition["sodium"] * 1.1
        ]

    elif condition == "Obesity":

        filtered = filtered[
            filtered["caloric_value"] <= nutrition["caloric_value"] * 0.6
        ]

    elif condition == "Heart Disease":

        filtered = filtered[
            filtered["cholesterol"] <= 100
        ]

    return filtered

def apply_diet_filter(food_df, patient):

    diet = patient["diet_type"]

    if diet == "Vegetarian":

        pattern = "|".join(NON_VEG)

        food_df = food_df[
            ~food_df["food"].str.lower().str.contains(
                pattern,
                na=False
            )
        ]

    return food_df

def apply_allergy_filter(food_df, patient):

    allergy = patient["allergy"]

    if allergy == "None":

        return food_df

    if allergy not in ALLERGY_MAP:

        return food_df

    pattern = "|".join(ALLERGY_MAP[allergy])

    return food_df[
        ~food_df["food"].str.lower().str.contains(
            pattern,
            na=False
        )
    ]

def apply_quality_filter(food_df):

    pattern = "|".join(LOW_QUALITY_FOODS+INVALID_FOODS)

    return food_df[
        ~food_df["food"].str.lower().str.contains(
            pattern,
            na=False
        )
    ]

def generate_candidates(food_df, patient, nutrition):

    foods = apply_health_rules(
        food_df,
        patient,
        nutrition
    )

    foods = apply_diet_filter(
        foods,
        patient
    )

    foods = apply_allergy_filter(
        foods,
        patient
    )

    foods = apply_quality_filter(
    foods
)

    return foods

def rank_foods(candidate_foods, nutrition, scaler):

    candidate_foods = candidate_foods[
        (candidate_foods["protein"] >= 5) &
        (candidate_foods["dietary_fiber"] >= 2) &
        (candidate_foods["caloric_value"] <= 500)
    ]

    nutrition_features = [
        "caloric_value",
        "protein",
        "carbohydrates",
        "fat",
        "dietary_fiber",
        "sugars",
        "sodium"
    ]

    # Patient vector
    patient_vector = scaler.transform(
        pd.DataFrame([nutrition])
    )

    # Food vectors
    food_vectors = scaler.transform(
        candidate_foods[nutrition_features]
    )

    # Cosine similarity
    similarities = cosine_similarity(
        patient_vector,
        food_vectors
    )[0]

    ranked = candidate_foods.copy()

    ranked["similarity_score"] = similarities

    # Nutrition distance
    ranked["nutrition_score"] = (
        abs(ranked["caloric_value"] - nutrition["caloric_value"]) +
        abs(ranked["protein"] - nutrition["protein"]) +
        abs(ranked["carbohydrates"] - nutrition["carbohydrates"]) +
        abs(ranked["fat"] - nutrition["fat"]) +
        abs(ranked["dietary_fiber"] - nutrition["dietary_fiber"])
    )

    # Normalize scores
    score_scaler = MinMaxScaler()

    ranked["similarity_norm"] = score_scaler.fit_transform(
        ranked[["similarity_score"]]
    )

    ranked["nutrition_norm"] = 1 - score_scaler.fit_transform(
        ranked[["nutrition_score"]]
    )

    #Find the food items that are suitable for meals
    pattern = "|".join(MEAL_KEYWORDS)

    ranked["meal_bonus"] = ranked["food"].str.lower().str.contains(
        pattern,
        na=False
    ).astype(int) * 0.05

    # Final score
    ranked["final_score"] = (
        0.7 * ranked["similarity_norm"] +
        0.3 * ranked["nutrition_norm"] +
        ranked["meal_bonus"]
    )

    # Penalize foods that are too calorie dense
    ranked.loc[
        ranked["caloric_value"] > 500,
        "final_score"
    ] -= 0.25

    # Penalize high fat foods
    ranked.loc[
        ranked["fat"] > 25,
        "final_score"
    ] -= 0.20

    # Penalize high sugar foods
    ranked.loc[
        ranked["sugars"] > 20,
        "final_score"
    ] -= 0.20

    # Penalize high sodium foods
    ranked.loc[
        ranked["sodium"] > 2.0,
        "final_score"
    ] -= 0.15

    ranked.loc[
        ranked["protein"] >= 15,
        "final_score"
    ] += 0.10

    ranked.loc[
        ranked["dietary_fiber"] >= 5,
        "final_score"
    ] += 0.10

    ranked = ranked.sort_values(
        "final_score",
        ascending=False
    )

    return ranked

def recommend_foods(patient_df, model, food_df, scaler, top_n=5):

    nutrition = predict_nutrition(model, patient_df)

    candidates = generate_candidates(
        food_df,
        patient_df,
        nutrition
    )

    ranked = rank_foods(
        candidates,
        nutrition,
        scaler
    )
    ranked = ranked.drop(
    columns=[
        "calorie_diff",
        "protein_diff",
        "carb_diff",
        "fat_diff",
        "fiber_diff",
        "similarity_norm",
        "nutrition_norm"
    ],
    errors="ignore"
)

    return ranked[
    [
        "food",
        "caloric_value",
        "protein",
        "carbohydrates",
        "fat",
        "dietary_fiber",
        "similarity_score",
        "final_score"
    ]
].head(top_n)

