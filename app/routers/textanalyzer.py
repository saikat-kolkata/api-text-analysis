from fastapi import HTTPException, APIRouter
# from pydantic import BaseModel
from typing import Dict
from dotenv import load_dotenv
from app.services import prompt_services
load_dotenv()

router = APIRouter()

# Data model for the request payload # NOT IN USE, AS PAYLOAD CHANGED FROM TEXT TO DIC
# class TextPayload(BaseModel):
#     text: str

# In-memory storage for processed text results
history = []


@router.post("/process")
def process_text(payload: Dict[str, str]):
    text = payload.get("text")
    if not text or not text.strip():
        raise HTTPException(status_code=400, detail="Text field cannot be empty.")

    mission = payload.get("mission")
    result_text = ""

    if mission == "summarize":
        result_text = prompt_services.get_summerize_text(text)
    
    elif mission == "named_entity":
        result_text = prompt_services.get_named_entity(text)
         
    elif mission == "sentiment":
        result_text = prompt_services.get_sentiment(text)

    else:
        raise HTTPException(status_code=400, detail="Invalid mission. Must be 'summarize', 'named_entity', or 'sentiment'.")
    
    return {"response": result_text,"code": 200}


@router.get("/history")
def get_history():
    """
    Retrieves all processed text results.
    """
    return {"history": history}