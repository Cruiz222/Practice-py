from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

FREE = [
    "openrouter/free",
    "cohere/north-mini-code:free",
    "invidia/nemotron.3.5-lightning:free",
    "minimax/minimax-m3.1-flash:free"
]

def call_free(prompt):
    for m in FREE:
        try:
            r = client.chat.completions.create(
                model=m,
                message=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.5
            )

            txt = r.choices[0].message.content
            if txt:
                return f"{m}\n{txt}"
        except Exception as e:
            print(f"{m} fail {e}")   

    return "no free message: check https://openrouter.ai for free models"             