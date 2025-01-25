# API Text Analysis

A FastAPI-based REST API service for text analysis using a large language model (LLM)

## Description

This project provides a web API service built with FastAPI that performs text analysis operations. The service exposes endpoints that allow users to analyze text through HTTP requests. Three features have been implemented - 
* Summarize the input text.
* Extract keywords or named entities.
* Provide sentiment analysis.

## Features

- RESTful API endpoints for text analysis
- Fast and asynchronous request handling
- Easy-to-use API interface

## Prerequisites

- Python 3.10 +

## Installation

1. Clone the repository:
```sh
git clone https://github.com/saikat-kolkata/api-text-analysis
cd api-text-analysis
```
## Create and activate a virtual environment (recommended):
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
## Install required dependencies:
```sh
pip install -r requirements.txt
```
## Usage : To run the server locally:
```sh
python main.py
The server will start on http://0.0.0.0:6080
```
## API Endpoints
| Endpoint | Remarks |
| ------ | ------ |
| GET / | Root endpoint for API testing |
| POST /process | Processes the input text based on the specified mission and returns the result after summerization / Entity recognition / sentiment analysis |
| GET /history | Retrieve all processed text results |

## File Structure
![image](https://github.com/user-attachments/assets/3f2e8194-a7a2-4295-b112-8611d22dc5cd)

| File | Details |
| ------ | ------ |
| main.py | Main file to start execution. Add all router modules here |
| requirements.txt | Requirement file, update if new packages added in the modules |
| .env | Environment variables, OpenAI API token is required to update here | 
| logfile.txt | Logs of all API calls input and output text |
| textanalyzer.py | Routers for text analysis |
| prompt_services.py | Supporting functions for the routers in integrate LLM response |
| prompt_utility.py | Basic utility functions that can be used as boiler plate for other service functions | 

## Output of Text Summerization API request with JSON input and output in Postman
![summerize](https://github.com/user-attachments/assets/b5760c50-0d1c-4612-8117-3e9422ea0a4e)

## Output of Named Entity Recognition API request with JSON input and output in Postman
![NE](https://github.com/user-attachments/assets/65f91fb1-331e-4b96-af1d-a5ae1611d366)

## Output of Sentiment Analysis API request with JSON input and output in Postman
![sentiment](https://github.com/user-attachments/assets/f459773c-dac9-4e3b-8968-986282daaea2)

## Output of history of all processed text results
![image](https://github.com/user-attachments/assets/9701e1b9-e070-4203-9958-1d4e0220f6e5)

## Output of API handling error
![error](https://github.com/user-attachments/assets/2a5e6027-deec-44a5-921b-52fd06aa45fd)



