from pydantic import BaseModel


class PatientRequest(BaseModel):            #define a shema for patient
    age: int
    gender: str
    height_m: float
    weight_kg: float
    bmi: float
    health_condition: str
    activity_level: str
    diet_type: str
    allergy: str