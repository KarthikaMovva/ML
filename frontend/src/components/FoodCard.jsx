function FoodCard({ food }) {

    return (

        <div className="bg-white rounded-xl shadow-lg p-5 hover:shadow-xl transition">

            <h2 className="text-xl font-bold text-emerald-700">

                🍽 {food.food}

            </h2>

            <div className="grid grid-cols-2 gap-3 mt-4">

                <p>Calories : <b>{food.caloric_value}</b></p>

                <p>Protein : <b>{food.protein} g</b></p>

                <p>Carbs : <b>{food.carbohydrates} g</b></p>

                <p>Fat : <b>{food.fat} g</b></p>

                <p>Fiber : <b>{food.dietary_fiber} g</b></p>

                <p>

                    Match :

                    <span className="text-green-600 font-bold">

                        {" "}
                        {(food.final_score * 100).toFixed(0)}%

                    </span>

                </p>

            </div>

        </div>

    );

}

export default FoodCard;