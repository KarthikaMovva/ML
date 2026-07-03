import { useState } from "react";
import api from "../../services/api";

function PatientForm({ setNutrition, setFoods }) {
    const [loading, setLoading] = useState(false);

    const calculateBMI = (height, weight) => {
        if (!height || !weight) return "";

        const bmi = weight / (height * height);

        return Number(bmi.toFixed(1));
    };

    const [form, setForm] = useState({
        age: 25,
        gender: "Male",
        height_m: 1.75,
        weight_kg: 72,
        bmi: calculateBMI(1.75, 72),
        health_condition: "Healthy",
        activity_level: "Medium",
        diet_type: "Vegetarian",
        allergy: "None"
    });

    const handleChange = (e) => {
        const { name, value } = e.target;

        let updatedForm = {
            ...form,
            [name]:
                name === "age" || name === "weight_kg"
                    ? Number(value)
                    : name === "height_m"
                        ? Number(value)
                        : value
        };

        if (name === "height_m" || name === "weight_kg") {
            updatedForm.bmi = calculateBMI(
                updatedForm.height_m,
                updatedForm.weight_kg
            );
        }

        setForm(updatedForm);
    };

    const submit = async (e) => {
        e.preventDefault();

        setLoading(true);

        try {
            const res = await api.post("/recommend", form);

            setNutrition(res.data.nutrition_targets);
            setFoods(res.data.recommendations);
        } catch (err) {
            console.log(err);
        }

        setLoading(false);
    };

    const inputStyle =
        "w-full rounded-lg border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition";

    return (
        <form
            onSubmit={submit}
            className="bg-white shadow-lg rounded-xl p-8"
        >
            <h2 className="text-2xl font-semibold text-gray-800 mb-6">
                Patient Information
            </h2>

            <div className="grid md:grid-cols-2 gap-5">

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Age
                    </label>

                    <input
                        className={inputStyle}
                        type="number"
                        name="age"
                        placeholder="Enter age"
                        value={form.age}
                        onChange={handleChange}
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Gender
                    </label>

                    <select
                        className={inputStyle}
                        name="gender"
                        value={form.gender}
                        onChange={handleChange}
                    >
                        <option>Male</option>
                        <option>Female</option>
                    </select>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Height (meters)
                    </label>

                    <input
                        className={inputStyle}
                        type="number"
                        step="0.01"
                        name="height_m"
                        placeholder="Example: 1.75"
                        value={form.height_m}
                        onChange={handleChange}
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Weight (kg)
                    </label>

                    <input
                        className={inputStyle}
                        type="number"
                        name="weight_kg"
                        placeholder="Example: 72"
                        value={form.weight_kg}
                        onChange={handleChange}
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        BMI (Auto Calculated)
                    </label>

                    <input
                        className={`${inputStyle} bg-gray-100`}
                        type="number"
                        value={form.bmi}
                        readOnly
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Health Condition
                    </label>

                    <select
                        className={inputStyle}
                        name="health_condition"
                        value={form.health_condition}
                        onChange={handleChange}
                    >
                        <option>Healthy</option>
                        <option>Diabetes</option>
                        <option>Hypertension</option>
                        <option>Heart Disease</option>
                        <option>Obesity</option>
                    </select>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Activity Level
                    </label>

                    <select
                        className={inputStyle}
                        name="activity_level"
                        value={form.activity_level}
                        onChange={handleChange}
                    >
                        <option>Low</option>
                        <option>Medium</option>
                        <option>High</option>
                    </select>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Diet Preference
                    </label>

                    <select
                        className={inputStyle}
                        name="diet_type"
                        value={form.diet_type}
                        onChange={handleChange}
                    >
                        <option>Vegetarian</option>
                        <option>Non Vegetarian</option>
                    </select>
                </div>

                <div className="md:col-span-2">
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Allergy
                    </label>

                    <select
                        className={inputStyle}
                        name="allergy"
                        value={form.allergy}
                        onChange={handleChange}
                    >
                        <option>None</option>
                        <option>Nut Allergy</option>
                        <option>Dairy Allergy</option>
                        <option>Seafood Allergy</option>
                    </select>
                </div>

            </div>

            <button
                type="submit"
                disabled={loading}
                className="mt-8 w-full rounded-xl bg-emerald-700 py-3 text-white font-semibold hover:bg-emerald-800 transition disabled:bg-emerald-400 disabled:cursor-not-allowed"
            >
                {loading
                    ? "Generating Recommendations..."
                    : "Generate Recommendations"}
            </button>
        </form>
    );
}

export default PatientForm;