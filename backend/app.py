from fastapi import FastAPI
from routers import flashcard

app = FastAPI()

app.include_router(flashcard.router)

@app.get("/")
async def root():
    return {"Message" : "Welcome to MainQuest"}