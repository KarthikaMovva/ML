function NutritionCard({ nutrition }) {

    const cards = [

        ["Calories", nutrition.caloric_value, "kcal"],

        ["Protein", nutrition.protein, "g"],

        ["Carbs", nutrition.carbohydrates, "g"],

        ["Fat", nutrition.fat, "g"],

        ["Fiber", nutrition.dietary_fiber, "g"],

        ["Sugar", nutrition.sugars, "g"],

        ["Sodium", nutrition.sodium, "mg"]

    ];

    return (

        <>

            <h2 className="text-2xl font-semibold mt-10 mb-5">

                Daily Nutrition Targets

            </h2>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-5">

                {

                    cards.map((item) => (

                        <div
                            key={item[0]}
                            className="bg-white rounded-xl shadow p-5 text-center"
                        >

                            <h3 className="text-gray-500">

                                {item[0]}

                            </h3>

                            <p className="text-2xl font-bold text-emerald-700 mt-2">

                                {item[1]}

                            </p>

                            <p className="text-gray-500">

                                {item[2]}

                            </p>

                        </div>

                    ))

                }

            </div>

        </>

    );

}

export default NutritionCard;