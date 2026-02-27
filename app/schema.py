from pydantic import BaseModel

class StudentData(BaseModel):
    University_GPA: float
    Internships_Completed: int
    Projects_Completed: int
    Certifications: int
    Soft_Skills_Score: float
    Networking_Score: float