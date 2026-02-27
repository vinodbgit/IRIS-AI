🚀 IRIS-AI
🎓 Industry Readiness Evaluation System

AI-Powered Employability Assessment & Career Analytics Platform

🌟 Project Overview

IRIS-AI (Industry Readiness Intelligence System) is an AI-powered web application that evaluates a student's industry readiness using machine learning.

It predicts:

💰 Estimated Salary

📊 Industry Readiness Index (IRI) (0–100)

🎯 Readiness Level (Low / Moderate / High)

🔍 Feature Contribution (Explainable AI)

📈 Progress Trend Analysis

📄 Downloadable Analytics Report

This system bridges the gap between academic performance and industry expectations.

🧠 Problem Statement

Students often:

Do not know their employability level

Lack measurable career readiness evaluation

Cannot track progress improvement

Receive no AI-based explainable insights

There is no unified platform that quantifies readiness using AI.

💡 Proposed Solution

IRIS-AI provides:

✔ AI-based salary prediction
✔ Industry Readiness Index calculation
✔ Explainable AI (Feature Contribution Analysis)
✔ Color-coded Gauge Visualization
✔ Student Progress Tracking
✔ Full Analytics PDF Export
✔ Cloud Deployment Ready

🏗 System Architecture

User Input
⬇
Data Preprocessing (Scaling)
⬇
Neural Network Prediction
⬇
IRI Calculation (0–100 Scale)
⬇
Explainability Analysis
⬇
Dashboard Visualization + Database Storage

⚙️ Technologies Used
Category	Technology
Programming	Python
ML Framework	TensorFlow
Data Scaling	Scikit-learn
Explainability	SHAP
Web UI	Streamlit
Database	SQLite
Deployment	GitHub + Streamlit Cloud
📂 Project Structure
IRIS-AI/
│
├── app/                # Backend prediction logic
├── data/               # Dataset
├── models/             # Trained model & scaler
├── src/                # Training scripts
├── dashboard.py        # Streamlit UI
├── requirements.txt    # Dependencies
├── README.md
└── .gitignore
🚀 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/vinodbgit/IRIS-AI.git
cd IRIS-AI
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
streamlit run dashboard.py

Open in browser:

http://localhost:8501
🌐 Live Deployment

🔗 GitHub Repository:
https://github.com/vinodbgit/IRIS-AI

🔗 Live App:
(Add your Streamlit Cloud URL here)

📊 Features
🎯 Industry Readiness Index (IRI)

Converts predicted salary into 0–100 scale

Classifies readiness level

Color-coded gauge meter

🔍 Explainable AI

Shows feature contribution

Transparency in predictions

📈 Progress Tracking

Stores prediction history

Displays trend graph

Shows statistics (avg, highest, lowest)

📄 Analytics Report

Generates downloadable PDF report

Includes summary statistics

🧮 Algorithm

Collect student input

Normalize using StandardScaler

Predict salary using Neural Network

Convert salary to IRI

Classify readiness level

Store results in SQLite database

Generate explainability insights

📸 Screenshots

(Add your dashboard screenshots here)

🔮 Future Scope

Resume Analyzer Integration

Job Role Recommendation Engine

Career Path Prediction

AI Career Chatbot

Cloud Database Integration

Multi-user Authentication

📚 References

TensorFlow Documentation

Scikit-learn Documentation

SHAP Explainability Paper

Streamlit Documentation

👨‍💻 Author

Vinod Badiger,
CSE Student,
AI & Machine Learning Enthusiast
