from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Model for incoming requests
class FixRequest(BaseModel):
    system_info: str
    issue: str

@app.get("/")
def home():
    return {"status": "FixPilot backend is running"}

@app.post("/diagnose")
def diagnose(request: FixRequest):
    # Basic example logic — replace with your AI call later
    return {
        "received_system_info": request.system_info,
        "received_issue": request.issue,
        "diagnosis": "Preliminary analysis complete. AI module not connected yet."
    }
