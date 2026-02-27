import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

def preprocess_data(filepath):
    df = pd.read_csv(filepath)

    # Select ONLY required features
    selected_features = [
        "University_GPA",
        "Internships_Completed",
        "Projects_Completed",
        "Certifications",
        "Soft_Skills_Score",
        "Networking_Score"
    ]

    X = df[selected_features]
    y = df["Starting_Salary"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    os.makedirs("models", exist_ok=True)
    joblib.dump(scaler, "models/scaler.pkl")

    return X_scaled, y