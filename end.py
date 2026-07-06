from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My API"


@app.route("/student")
def student():

    return jsonify({
        "name": "Sri Raam",
        "age": 22
    })


@app.route("/college")
def college():

    return jsonify({
        "college": "VIT",
        "city": "Vellore"
    })


@app.route("/skills")
def skills():

    return jsonify({
        "skills": [
            "Python",
            "SQL",
            "Machine Learning",
            "Flask"
        ]
    })


app.run(debug=True)