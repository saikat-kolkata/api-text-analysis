from fastapi import HTTPException
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key= os.getenv("APIKEY")
)


def get_summerize_text(text:str):

    result_text = None
    try:                
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                    {"role": "user", "content": f"Summarize the following text:\n{text}"}
                ],
            max_tokens=500,
            temperature=0.8
        )
        result_text = response.choices[0].message.content
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")
    
    return result_text

def get_named_entity(text:str):
    
    result_text = None
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": system_message_named_entity()},
                    {"role": "user", "content": f"{assisstant_message()}.Now extract keywords or named entities from following text:\n{text}"}
                ],
            max_tokens=100,
            temperature=0.5
        )
        result_text = response.choices[0].message.content
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")
    return result_text
    
def get_sentiment(text:str):

    result_text = None
    try:    
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a helpful assistant that identify the sentiment of a text"},
                    {"role": "user", "content": f"Mention only Positive or Negative as a sentiment for the following text:\n{text}"}
                ],
            max_tokens=100,
            temperature=0.5
        )
        result_text = response.choices[0].message.content
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")
    return result_text