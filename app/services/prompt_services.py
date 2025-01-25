from fastapi import HTTPException
from openai import OpenAI
from dotenv import load_dotenv
from app.util import prompt_utility
import json
import os

load_dotenv()

#Initialize OpenAI client
client = OpenAI(
    api_key= os.getenv("APIKEY")
)


def get_summerize_text(text:str):
    """
    Summerize the input text using OpenAI API and return the result
    Args:
        text (str): Input string to be used for summerization
    Returns:
        result_text (str) : Summerized text
    Raises:
        HTTPException: If processing fails from the OpenAI API
    """
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
    """
    Identify name and entity from the input text using OpenAI API and return the result
    Args:
        text (str): Input string to be used for identifing name and entity
    Returns:
        result_text (str) : Identified name and entity text
    Raises:
        HTTPException: If processing fails from the OpenAI API
    """
    result_text = None
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": prompt_utility.system_message_named_entity()},
                    {"role": "user", "content": f"{prompt_utility.assisstant_message()}.Now extract keywords or named entities from following text:\n{text}"}
                ],
            max_tokens=100,
            temperature=0.5
        )
        result_text = response.choices[0].message.content
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")
    return result_text
    
def get_sentiment(text:str):
    """
    Get sentiment from the input text using OpenAI API and return the result
    Args:
        text (str): Input string to be used for identifing sentiment
    Returns:
        result_text (str) : Identified name and entity text
    Raises:
        HTTPException: If processing fails from the OpenAI API
    """
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

def write_to_log_file(input_data: dict, log_file: str = "logfile.txt"):
    """
    Writes the input data dictionary to a log file in JSON format.

    Args:
        input_data (dict): Dictionary containing input text, mission, and output.
        log_file (str): The file where the log will be stored. 
    """
    try:
        # Open the log file in append mode
        with open(log_file, "a") as file:
            file.write(json.dumps(input_data) + "\n")
        print("Log entry successfully written.")
    except Exception as e:
        print(f"An error occurred while writing to the log file: {e}")


def read_log_file(log_file: str = "logfile.txt"):
    """
    Reads the log file and returns the contents as a list of dictionaries.

    Args:
        log_file (str): The file from which the log will be read.

    Returns:
        list: A list of dictionaries containing the logged data.
    """
    try:
        with open(log_file, "r") as file:
            logs = [json.loads(line.strip()) for line in file if line.strip()]
        return logs
    except FileNotFoundError:
        print(f"The file '{log_file}' does not exist.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from the file: {e}")
        return []
