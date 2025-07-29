# ProjectDataAnalysis2025_PartC
 Flask-based web application for predicting apartment rental prices in Tel Aviv using machine learning. The model is trained on historical listings data and supports multiple apartment features as input.


# 🏠 Tel Aviv Apartment Rent Price Predictor

A Flask-based web application for predicting apartment rental prices in Tel Aviv–Yafo using a trained machine learning model.

---

## 📁 Project Structure

```
flask_rent_app/
├── api.py                  # Flask API for serving predictions
├── model_training.py       # Script to preprocess data and train the model
├── trained_model.pkl       # Serialized model (via joblib)
├── train.xlsx              # Dataset for training
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Web form UI
```

---

## ⚙️ Technologies

- Python 3.12+
- Flask
- pandas
- scikit-learn
- joblib
- HTML5 / CSS3 (RTL)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask_rent_app.git
cd flask_rent_app
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model (if not already trained)

```bash
python model_training.py
```

This will create `trained_model.pkl`.

### 5. Run the Flask app

```bash
python api.py
```

Then open your browser at:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Features Used in Prediction

The following features are used for rent prediction:

- `property_type`
- `neighborhood`
- `room_num`
- `floor`
- `area`
- `garden_area`
- `has_parking`
- `has_storage`
- `elevator`
- `ac`
- `handicap`
- `has_bars`
- `has_safe_room`
- `has_balcony`
- `is_furnished`
- `is_renovated`
- `distance_from_center`

---

## 🖥️ Web Interface

- Clean, modern RTL (Hebrew) layout
- Dropdowns for `property_type` and `neighborhood` based on dataset
- Validated numeric fields (range, step)
- Boolean checkboxes for additional features
- Displays estimated rent after submission

---

## 📄 License

This project is provided for educational use only.  
No commercial license or warranty provided.
