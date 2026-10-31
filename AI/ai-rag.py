from openai import OpenAi 
import os 
from dotenv import load_dotenv

load_dotenv()

client = OpenAi(base_url=https://openrouter.ai/free/v1, api_key=os.getenv("OPENROUTER_API_KEY"))

FREE = [
    "openrouter/free",
    "cohere/north-mini-code:free",
    "invidia/nemotron-3-ultra-550b-a55b:free",
    "invidia/nemotron-3.5-lightning:free"
]

def ai_chat(p):
    for m in FREE:
        try:
            resp = client.chat.completions.create(
                model=m,
                message=[{"role": "user", "content": p}],
                max_tokens=300,
                temperature=0.3
            )
            if resp.choices[0].message.content:
                return resp.choices[0].message.content
        except Exception as e:
            print(f"{m} failed {e}")
    return "couldn't generate and answer, try again"                