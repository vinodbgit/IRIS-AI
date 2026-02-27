from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///students.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class StudentProgress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)
    iri_score = Column(Float)

Base.metadata.create_all(engine)