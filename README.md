# ProjectDataAnalysis2025_PartC
 Flask-based web application for predicting apartment rental prices in Tel Aviv using machine learning. The model is trained on historical listings data and supports multiple apartment features as input.


# Real Estate Rent Price Predictor – Tel Aviv 🏙️  
*Final Project – Data Analyst Course 2025 | Part 3*

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange?logo=scikitlearn)]
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🧾 About the Project

This repository contains Part 3 of the **final assignment** for the **Data Analyst Course (2025)**.

In this stage, we develop and deploy a **machine learning model** that predicts rental prices for apartments in **Tel Aviv** using a selected subset of features from the cleaned dataset created in Part 1.

The model is deployed via a **Flask web app**, where users can input apartment details and receive a rental price prediction.

---

## ⚙️ Key Features

- Cleaned & preprocessed input data from `.xlsx` file
- Feature selection based on relevance to price
- Trained **Elastic Net** and **Tree-based** models for comparison
- Final model serialized using `joblib`
- Deployed via **Flask** backend + **HTML/CSS** frontend
- Supports real-time rental price prediction via browser interface

---

## 📂 Project Structure

```
├── api.py               # Flask backend logic (prediction API)
├── model_training.py    # Model training & joblib export
├── templates/
│   └── index.html       # User interface (form & results)
├── train.xlsx           # Input dataset
├── trained_model.pkl    # Trained ML model
└── README.md            # Project documentation
```

---

## 🧠 Features Used in the Model

Only the following fields were used for prediction:

| Feature               | Description                                 |
|-----------------------|---------------------------------------------|
| `property_type`       | Type of apartment                           |
| `neighborhood`        | Neighborhood in Tel Aviv                    |
| `room_num`            | Number of rooms                             |
| `floor`               | Apartment floor                             |
| `area`                | Size in square meters                       |
| `garden_area`         | Garden size                                 |
| `has_parking`         | Has parking (0/1)                           |
| `has_storage`         | Has storage (0/1)                           |
| `elevator`            | Has elevator (0/1), only relevant if `total_floors` > 2 |
| `ac`                  | Has air conditioning (0/1)                  |
| `handicap`            | Handicap accessible (0/1)                   |
| `has_bars`            | Has bars on windows (0/1)                   |
| `has_safe_room`       | Has protected room (0/1)                    |
| `has_balcony`         | Has balcony (0/1)                           |
| `is_furnished`        | Furnished (0/1)                             |
| `is_renovated`        | Renovated (0/1)                             |
| `distance_from_center`| Distance from city center (km)             |

---

## 🚀 How to Run Locally

1. Clone the repository  
```bash
git clone https://github.com/your-username/rent-predictor-tel-aviv.git
cd rent-predictor-tel-aviv
```

2. Create a virtual environment and activate  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. Install dependencies  
```bash
pip install -r requirements.txt
```

4. Train the model (optional)  
```bash
python model_training.py
```

5. Run the web app  
```bash
python api.py
```

6. Open in your browser  
Visit [http://localhost:5000](http://localhost:5000)

---

## 📃 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
