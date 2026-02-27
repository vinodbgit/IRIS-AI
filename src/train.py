from preprocessing import preprocess_data
from model import build_model
from sklearn.model_selection import train_test_split
import tensorflow as tf
import os

X, y = preprocess_data("data/education_career_success.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = build_model(X_train.shape[1])

model.fit(X_train, y_train, epochs=50, batch_size=16)

os.makedirs("models", exist_ok=True)
model.save("models/nn_model.h5")

print("Model training completed successfully!")