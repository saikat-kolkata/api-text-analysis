from fastapi import FastAPI

fastapp = FastAPI() #initiate fastapi

@fastapp.get("/") #get request
def home():
    return {"Response": "Test root API"}