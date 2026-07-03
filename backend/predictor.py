import pandas as pd


def predict_nutrition(model, patient):                       #can refer notebooks for core logic

    patient_df = pd.DataFrame([patient])

    prediction = model.predict(patient_df)

    return {
        "caloric_value": prediction[0][0],
        "protein": prediction[0][1],
        "carbohydrates": prediction[0][2],
        "fat": prediction[0][3],
        "dietary_fiber": prediction[0][4],
        "sugars": prediction[0][5],
        "sodium": prediction[0][6]
    }