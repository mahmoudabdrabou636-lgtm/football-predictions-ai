from fastapi import FastAPI

app = FastAPI(
    title="Football Predictions AI",
    description="AI-powered football match prediction and analysis platform",
    version="0.1.0"
)


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
