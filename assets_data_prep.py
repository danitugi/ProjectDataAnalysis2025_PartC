import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer



def prepare_data(df):
    """
    קולט DataFrame יחיד מהטופס ומחזיר רק את העמודות הדרושות למודל.
    """
    selected_columns = [
        "property_type", "neighborhood", "room_num", "floor", "area", "garden_area",
        "has_parking", "has_storage", "elevator", "ac", "handicap", "has_bars",
        "has_safe_room", "has_balcony", "is_furnished", "is_renovated", "distance_from_center"
    ]

    for col in selected_columns:
        if col not in df.columns:
            df[col] = 0  # מילוי ברירת מחדל אם חסר בטופס

    return df[selected_columns]