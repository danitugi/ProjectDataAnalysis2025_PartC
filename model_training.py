from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import ElasticNet
import pandas as pd
import joblib

# Load data
df = pd.read_excel("train.xlsx")
selected_features = [
    "property_type", "neighborhood", "room_num", "floor", "area", "garden_area",
    "has_parking", "has_storage", "elevator", "ac", "handicap", "has_bars",
    "has_safe_room", "has_balcony", "is_furnished", "is_renovated", "distance_from_center"
]
target = "price"

df = df[selected_features + [target]].copy()

# Drop rows where the target is missing
df.dropna(subset=[target], inplace=True)

X = df[selected_features]
y = df[target]

# Split columns
numeric_features = ["room_num", "floor", "area", "garden_area", "distance_from_center"]
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_features = [
    "property_type", "neighborhood",
    "has_parking", "has_storage", "elevator", "ac", "handicap", "has_bars",
    "has_safe_room", "has_balcony", "is_furnished", "is_renovated"
]
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# Combine preprocessors
preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# Final pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", ElasticNet(alpha=0.1, l1_ratio=0.5))
])

# Fit model
model.fit(X, y)

# Save model
joblib.dump(model, "trained_model.pkl")
print("Model trained and saved to 'trained_model.pkl'")