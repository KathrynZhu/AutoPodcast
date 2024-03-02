# main.py
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route
from api.elevenlabs_api import *  # This imports your ElevenLabs-related handlers
from api.openai_api import generate_text_from_openai  # Import OpenAI API handler

routes = [
    # Your existing routes...
    Route("/generate-text", generate_text_from_openai, methods=["POST"]),
    
    Route("/create", create, methods=["POST"]),
    Route("/status/{job_id}", status, methods=["GET"]),
    Route("/speech/{job_id}", speech, methods=["GET"]),
    Route("/files", files, methods=["GET"])
]

app = Starlette(debug=True, routes=routes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# The rest of your Starlette application setup...
