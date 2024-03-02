# api/openai_api.py
import openai
from starlette.responses import JSONResponse
import asyncio
import os
import requests
import uuid

# Assuming you have set OPENAI_API_KEY as an environment variable
#openai.api_key = os.getenv("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")
openai.api_key = os.getenv("OPENAI_API_KEY")


async def generate_text_from_openai(request):
    data = await request.json()
    prompt = data.get("prompt")

    print("in api file" + prompt)
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        message = response.choices[0].message
        return JSONResponse({"message": message})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
