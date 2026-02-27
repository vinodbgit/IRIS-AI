import numpy as np
import tensorflow as tf
import joblib
import shap

# Load trained model
model = tf.keras.models.load_model("models/nn_model.h5", compile=False)

# Load scaler
scaler = joblib.load("models/scaler.pkl")

# Feature names (must match training order)
feature_names = [
    "University_GPA",
    "Internships_Completed",
    "Projects_Completed",
    "Certifications",
    "Soft_Skills_Score",
    "Networking_Score"
]

# Create small background dataset for SHAP (required)
background_data = np.zeros((10, 6))  # 10 samples, 6 features
explainer = shap.Explainer(model, background_data)


def predict_salary(data):

    # Convert input dictionary to numpy array
    input_data = np.array([[
        data["University_GPA"],
        data["Internships_Completed"],
        data["Projects_Completed"],
        data["Certifications"],
        data["Soft_Skills_Score"],
        data["Networking_Score"]
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict salary
    prediction = model.predict(input_scaled)
    salary = prediction[0][0]

    # Normalize salary to 0–100 Industry Readiness Index
    min_salary = 0
    max_salary = 1000000  # Adjust if needed based on dataset

    iri = ((salary - min_salary) / (max_salary - min_salary)) * 100
    iri = max(0, min(iri, 100))  # Clamp between 0–100

    # Determine readiness level
    if iri < 40:
        level = "Low"
    elif iri < 70:
        level = "Moderate"
    else:
        level = "High"

    # Calculate SHAP feature contributions
    shap_values = explainer(input_scaled)

    contributions = {
    feature_names[i]: round(
        float((shap_values.values[0][i] / 1000000) * 100), 4
    )
    for i in range(len(feature_names))
}

    return {
        "Predicted_Salary": round(float(salary), 2),
        "Industry_Readiness_Index": round(float(iri), 2),
        "Readiness_Level": level,
        "Feature_Contributions": contributions
    }