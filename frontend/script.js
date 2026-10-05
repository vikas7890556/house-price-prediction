const form = document.getElementById("predictionForm");

const result = document.getElementById("result");
const price = document.getElementById("price");
const error = document.getElementById("error");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    result.classList.add("hidden");
    error.classList.add("hidden");

    const houseData = {
        bedrooms: Number(document.getElementById("bedrooms").value),
        bathrooms: Number(document.getElementById("bathrooms").value),
        sqft_living: Number(document.getElementById("sqft_living").value),
        sqft_lot: Number(document.getElementById("sqft_lot").value),
        floors: Number(document.getElementById("floors").value),
        waterfront: Number(document.getElementById("waterfront").value),
        view: Number(document.getElementById("view").value),
        condition: Number(document.getElementById("condition").value),
        grade: Number(document.getElementById("grade").value),
        sqft_above: Number(document.getElementById("sqft_above").value),
        sqft_basement: Number(document.getElementById("sqft_basement").value),
        yr_built: Number(document.getElementById("yr_built").value),
        sqft_living15: Number(document.getElementById("sqft_living15").value),
        lat: Number(document.getElementById("lat").value),
        long: Number(document.getElementById("long").value),
        zipcode: Number(document.getElementById("zipcode").value)
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(houseData)
            }
        );

        if (!response.ok) {
            throw new Error("Prediction request failed.");
        }

        const data = await response.json();

        price.textContent =
            "$" + data.predicted_price.toLocaleString("en-US", {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });

        result.classList.remove("hidden");

    } catch (err) {

        error.textContent =
            "Unable to connect to the prediction server.";

        error.classList.remove("hidden");

        console.error(err);
    }

});