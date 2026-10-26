import os
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()
app = FastAPI()

client = Groq(os.getenv("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    query: str
    budget_data: str = ""

@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message": "Budget Manager API running now"
    }

@app.post("/ai/chat")
def ai_chat(req: ChatRequest):
    prompt = f"""
    - you are a financial assistant, you are to give financial advice to users.
    -you are to give five helpful tips atleast
    - you are to be honest but encouraging

    user query: {req.query}
    message: answer {req.budget_data if budget_data else "budget data is not yet available, give general advice"}
    """ 

    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b"
        message=[{"role": "user", "content": req.query}]
    )

    return {
        "query": req.query,
        "answer": completion.choices[0].message.content
    }


@app.get("/")
def route():
    return {
        "message": "budget manager API is running now"
        "docs": "/docs"
        "health": "/health"
        "ai_chat": "/ai/chat (post)"
    }    

