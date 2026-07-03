import { useState } from "react";
import PatientForm from "./components/PatientForm";
import NutritionCard from "./components/NutritionCard";
import FoodList from "./components/FoodList";

function App() {

  const [nutrition, setNutrition] = useState(null);
  const [foods, setFoods] = useState([]);

  return (

    <div className="min-h-screen bg-slate-100">

      <header className="bg-emerald-700 text-white shadow-md">

        <div className="max-w-6xl mx-auto py-6">

          <h1 className="text-4xl font-bold text-center">

            🥗 My_Nutritionist

          </h1>

          <p className="text-center text-emerald-100 mt-2">

            AI Powered Personalized Nutrition Recommendation System

          </p>

        </div>

      </header>

      <div className="max-w-6xl mx-auto p-8">

        <PatientForm
          setNutrition={setNutrition}
          setFoods={setFoods}
        />

        {nutrition &&

          <NutritionCard nutrition={nutrition} />

        }

        {foods.length > 0 &&

          <FoodList foods={foods} />

        }

      </div>

    </div>

  );

}

export default App;