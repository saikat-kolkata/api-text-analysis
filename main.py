from fastapi import FastAPI
import uvicorn

from app.routers import textanalyzer

fastapp = FastAPI() #initiate fastapi

fastapp.include_router(textanalyzer.router)

@fastapp.get("/") 
#get request testing
async def home():
    return {"Response": "Test root API"}


if __name__ == "__main__":
    uvicorn.run(fastapp, host="0.0.0.0", port=6080, forwarded_allow_ips="*")