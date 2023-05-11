import pandas as pd
import joblib
import sklearn
from flask import Flask, jsonify, request
import os
import gunicorn

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def homepage():
    return "Welcome! Navigate to /predict?x0=num&x1=num to view the prediction. Please change both 'num' to the input values."

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    x0 = float(request.args.get("x0"))
    x1 = float(request.args.get("x1"))
    model = joblib.load("model/lr.joblib")
    df = pd.DataFrame({"x0":float(x0), "x1":float(x1)}, index = [0])

    y_pred = model.predict(df)

    result = {"prediction":y_pred[0]}

    return jsonify(result)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8088)
