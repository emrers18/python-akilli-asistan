from fastapi import FastAPI
from pydantic import BaseModel

from assistant_logic import fake_smart_assistant
from database import create_table, save_message, get_all_messages

app = FastAPI()

create_table()

class MessageRequesst(BaseModel):
    user_message:str

@app.get("/")
def home():
    return {
        "message":"Akıllı Asistan API çalışıyor",
        "status":"ok"
    }


@app.post("/chat")
def chat_with_assistant(request:MessageRequesst):
    user_message = request.user_message

    assistant_response = fake_smart_assistant(user_message)

    save_message(user_message, assistant_response)

    return {
        "user_message": user_message,
        "assistant_response": assistant_response
    }

@app.get("/messages")
def read_all_messages():
    messages = get_all_messages()
    return {
        "messages": messages
    }
