import FoodCard from "./FoodCard";

function FoodList({ foods }) {

    return (

        <>

            <h2 className="text-2xl font-semibold mt-10 mb-5">

                Recommended Foods

            </h2>

            <div className="grid md:grid-cols-2 gap-5">

                {

                    foods.map((food, index) => (

                        <FoodCard
                            key={index}
                            food={food}
                        />

                    ))

                }

            </div>

        </>

    );

}

export default FoodList;