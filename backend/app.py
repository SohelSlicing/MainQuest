#uvicorn app:app --reload

from fastapi import FastAPI
from pydantic import BaseModel

from routers import flashcard

app = FastAPI()

app.include_router(flashcard.router)

class generate(BaseModel):
    text: str
    number: int

@app.get("/")
def root():
    return {"message" : "Main app file"}

@app.post("/post")
def test_post(post: generate):
    return {"message" : "param passed"}
