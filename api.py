from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# טען את המודל המאומן
with open("trained_model.pkl", "rb") as f:
    model = joblib.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # רשימת שדות בוליאניים
    binary_fields = [
        "has_parking", "has_storage", "elevator", "ac", "handicap",
        "has_bars", "has_safe_room", "has_balcony", "is_furnished", "is_renovated"
    ]

    # טען את השדות מהטופס (עם ברירת מחדל 0 ל־checkboxes)
    data = {
        "property_type": request.form.get("property_type"),
        "neighborhood": request.form.get("neighborhood"),
        "room_num": request.form.get("room_num"),
        "floor": request.form.get("floor"),
        "area": request.form.get("area"),
        "garden_area": request.form.get("garden_area"),
        "distance_from_center": request.form.get("distance_from_center"),
    }

    # הוסף את השדות הבוליאניים עם ברירת מחדל 0
    for field in binary_fields:
        data[field] = request.form.get(field, "0")

    # המרת כל השדות המתאימים לסוגים
    df = pd.DataFrame([data])

    numeric_fields = ["room_num", "floor", "area", "garden_area", "distance_from_center"]
    for field in numeric_fields:
        df[field] = pd.to_numeric(df[field], errors="coerce")

    for field in binary_fields:
        df[field] = df[field].apply(lambda x: 1 if x in ["1", "on", True] else 0)

    # בצע תחזית
    prediction = model.predict(df)[0]
    prediction = round(prediction, 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
