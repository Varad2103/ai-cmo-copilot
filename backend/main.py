from fastapi import FastAPI

app = FastAPI(
    title="AI CMO Copilot",
    description="Marketing intelligence and executive decision-support API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "AI CMO Copilot API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }