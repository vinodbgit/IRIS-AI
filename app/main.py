from fastapi import FastAPI
from app.schema import StudentData
from app.predictor import predict_salary
from app.database import Session, StudentProgress

app = FastAPI(title="IRIS-AI API")

@app.get("/")
def home():
    return {"message": "IRIS-AI is running"}

@app.post("/predict")
def predict(data: StudentData):

    result = predict_salary(data.dict())

    session = Session()
    new_record = StudentProgress(
        iri_score=result["Industry_Readiness_Index"]
    )
    session.add(new_record)
    session.commit()

    return result