from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("iris_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = [[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]]

    flower_names = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    prediction = model.predict(features)[0]

    return jsonify({
        "prediction": flower_names[int(prediction)]
    })

app.run(debug=True)
print("Git Learning")
print("Feature Branch")