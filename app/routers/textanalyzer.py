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


@router.post("/process")
async def process_text(payload: Dict[str, str]):

    """
    Processes the input text based on the specified mission and returns the result.

    Args:
        payload (Dict[str, str]): A dictionary containing:
            - "text" (str): The input text to be processed.
            - "mission" (str): The task to perform on the text. 
              Must be one of the following:
                - "summarize": Summarizes the input text.
                - "named_entity": Extracts named entities from the input text.
                - "sentiment": Performs sentiment analysis on the input text.

    Returns:
        dict: A response containing:
            - "response" (str): The result of the requested mission.
            - "code" (int): HTTP status code (200 for success).

    Raises:
        HTTPException: If the "text" field is empty, or the "mission" field 
                       is invalid, an appropriate HTTPException with status code 400 is raised.

    Details of functions:
        - For "summarize", the function calls `prompt_services.get_summerize_text` 
          to summarize the input text.
        - For "named_entity", the function calls `prompt_services.get_named_entity` 
          to extract named entities.
        - For "sentiment", the function calls `prompt_services.get_sentiment` 
          to analyze the sentiment of the input text.

    Logging:
        - Logs the input text, mission, and output result into a log file using 
          `prompt_services.write_to_log_file`.

    Example Payload:
        {
            "text": "FastAPI is a modern web framework for Python.",
            "mission": "summarize"
        }

    Example Response:
        {
            "response": "FastAPI is a web framework.",
            "code": 200
        }
    """
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
    
    # Logging the details of input text and output text to a file for future use
    log_dic = {}
    log_dic["input_text"] = text
    log_dic["mission"] = mission
    log_dic["output"] = result_text

    prompt_services.write_to_log_file(log_dic)

    return {"response": result_text,"code": 200}


@router.get("/history")
async def get_history():
    """
    Retrieve the history of prompts from the log file.

    This endpoint fetches the logged history of prompts that were previously
    processed by the system. The data is read from a log file and returned 
    as a response in JSON format.
    Args:
        None
    Returns:
        dict: A dictionary containing the prompt history and a status code.
            - "history": The content of the log file with the processed prompts.
            - "code": The HTTP status code, which is always 200 for successful retrieval.

    Raises:
        HTTPException: If there is an error during the process of reading the log file.
    Details of functions:
        - For reading logs, the function calls `prompt_services.read_log_file` 
    """
    history = prompt_services.read_log_file()
    return {"history": history,"code": 200}