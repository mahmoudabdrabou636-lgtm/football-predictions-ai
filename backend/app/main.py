from fastapi import FastAPI
from database.connection import engine, Base

app = FastAPI(
    title="Football Predictions AI",
    description="AI-powered football match prediction and analysis platform",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "project": "Football Predictions AI",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
