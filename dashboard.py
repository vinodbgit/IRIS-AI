import streamlit as st
from app.predictor import predict_salary
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import time
import sqlite3
import pandas as pd
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

st.set_page_config(page_title="IRIS-AI Dashboard", layout="centered")

st.title("🎓 IRIS-AI Industry Readiness Dashboard")
st.markdown("AI-Powered Employability Evaluation & Analytics System")

# ---------------- DATABASE INITIALIZATION (CLOUD SAFE) ----------------
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            iri_score REAL
        )
    """)
    conn.commit()
    conn.close()

init_db()

st.divider()

# ---------------- INPUT SECTION ----------------
st.subheader("📌 Enter Student Details")

gpa = st.number_input("University GPA", 0.0, 10.0, step=0.1)
internships = st.number_input("Internships Completed", 0)
projects = st.number_input("Projects Completed", 0)
certifications = st.number_input("Certifications", 0)
soft_skills = st.number_input("Soft Skills Score", 0.0, 10.0, step=0.1)
networking = st.number_input("Networking Score", 0.0, 10.0, step=0.1)

col1, col2 = st.columns(2)
predict_clicked = col1.button("🚀 Predict")
reset_clicked = col2.button("🔄 Reset")

if reset_clicked:
    st.rerun()

# ---------------- PREDICTION ----------------
if predict_clicked:

    data = {
        "University_GPA": gpa,
        "Internships_Completed": internships,
        "Projects_Completed": projects,
        "Certifications": certifications,
        "Soft_Skills_Score": soft_skills,
        "Networking_Score": networking
    }

    # Progress animation
    progress = st.progress(0)
    for percent in range(100):
        time.sleep(0.01)
        progress.progress(percent + 1)

    result = predict_salary(data)

    salary = result["Predicted_Salary"]
    iri = result["Industry_Readiness_Index"]
    level = result["Readiness_Level"]
    contributions = result["Feature_Contributions"]

    # Save to DB
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO progress (iri_score) VALUES (?)", (iri,))
    conn.commit()
    conn.close()

    st.success("Prediction Completed ✅")

    # ---------------- GAUGE ----------------
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=iri,
        title={'text': "Industry Readiness Index"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 40], 'color': "#ff4b4b"},
                {'range': [40, 70], 'color': "#ffa500"},
                {'range': [70, 100], 'color': "#00c853"}
            ],
        }
    ))
    st.plotly_chart(gauge, use_container_width=True)

    st.markdown(f"""
    💰 **Predicted Salary:** ₹ {salary}  
    🎯 **Readiness Level:** {level}
    """)

    # ---------------- SHAP / FEATURE IMPACT ----------------
    st.subheader("🔍 Feature Impact")
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.barh(list(contributions.keys()), list(contributions.values()))
    st.pyplot(fig)

    # ---------------- CONCLUSION ----------------
    st.subheader("📝 Conclusion")
    if level == "High":
        st.success("Strong industry readiness with high employability potential.")
    elif level == "Moderate":
        st.warning("Moderate readiness. Improving practical exposure can enhance career outcomes.")
    else:
        st.error("Low readiness. Skill development and internships are recommended.")

# ---------------- HISTORY & TREND ----------------
st.divider()
st.subheader("📊 Prediction History & Trend Analysis")

clear_history = st.button("🗑 Clear Prediction History")

if clear_history:
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM progress")
    conn.commit()
    conn.close()
    st.success("Prediction history cleared successfully.")
    st.rerun()

conn = sqlite3.connect("students.db")
df = pd.read_sql("SELECT * FROM progress", conn)
conn.close()

if not df.empty:

    st.write("### IRI Trend Over Time")
    fig2, ax2 = plt.subplots(figsize=(6,3))
    ax2.plot(df["iri_score"], marker='o')
    ax2.set_ylabel("IRI Score")
    ax2.set_xlabel("Prediction Count")
    st.pyplot(fig2)

    st.write("### Summary Statistics")
    st.write(f"Total Predictions: {len(df)}")
    st.write(f"Average IRI: {round(df['iri_score'].mean(),2)}")
    st.write(f"Highest IRI: {round(df['iri_score'].max(),2)}")
    st.write(f"Lowest IRI: {round(df['iri_score'].min(),2)}")

    # ---------------- EXPORT FULL ANALYTICS REPORT ----------------
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("IRIS-AI Full Analytics Report", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    summary_data = [
        ["Total Predictions", str(len(df))],
        ["Average IRI", str(round(df["iri_score"].mean(),2))],
        ["Highest IRI", str(round(df["iri_score"].max(),2))],
        ["Lowest IRI", str(round(df["iri_score"].min(),2))]
    ]

    table = Table(summary_data)
    elements.append(table)

    elements.append(Spacer(1, 0.4 * inch))
    elements.append(Paragraph("Historical IRI Records:", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    history_table = Table(df.values.tolist())
    elements.append(history_table)

    doc.build(elements)

    st.download_button(
        label="📄 Download Full Analytics Report",
        data=buffer.getvalue(),
        file_name="IRIS_AI_Full_Analytics_Report.pdf",
        mime="application/pdf"
    )

else:
    st.info("No prediction history available yet.")