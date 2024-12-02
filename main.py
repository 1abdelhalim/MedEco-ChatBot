from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

openai.api_key = "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"

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

def generate_prompt(query: str) -> str:
    system_prompt = (
        "أنت مساعد ذكاء اصطناعي خبير في التفاعلات الدوائية وتفاعلات الدواء مع الطعام. "
        "تتحدث باللهجة المصرية وتقدم إجابات واضحة وبسيطة. "
        "إذا كان السؤال متعلقًا بالأكل أو التفاعلات، وضح الأسباب العلمية بطريقة مفهومة. "
        "إذا لم يكن لديك الإجابة، اعتذر بلباقة."
    )
    return f"{system_prompt}\n\nسؤال المستخدم: {query}\nالإجابة:"

@app.post("/query")
async def handle_query(request: QueryRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": "أنت مساعد ذكاء اصطناعي خبير في التفاعلات الدوائية."},
                {"role": "user", "content": request.query}
            ]
        )
        return {"response": response['choices'][0]['message']['content'].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))