from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_query
app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    response = process_query(request.message)

    return {
        "response": response
    }