# API Text Analysis

A FastAPI-based REST API service for text analysis using a large language model (LLM)

## Description

This project provides a web API service built with FastAPI that performs text analysis operations. The service exposes endpoints that allow users to analyze text through HTTP requests. Three features have been implemented - 
* Summarise the input text.
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

git clone [<repository-url>](https://github.com/saikat-kolkata/api-text-analysis)
cd api-text-analysis

## Create and activate a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

## Install required dependencies:
pip install -r requirements.txt

## Usage : To run the server locally:

python main.py

The server will start on http://0.0.0.0:6080

API Endpoints
GET /: Root endpoint for API testing
POST /process: Processes the input text based on the specified mission and returns the result after summerization / Entity recognition / sentiment analysis
GET /history: Retrieve all processed text results




