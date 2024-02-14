import asyncio
import elevenlabs
import os
import requests
import uuid
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, FileResponse
from starlette.background import BackgroundTasks
from starlette.routing import Route
import sys
from pydub import AudioSegment
from pydub.playback import play
from elevenlabs import voices

elevenlabs.set_api_key("41b70d01d548863403dcc1c9c6434582")

# Not sure how this is used with the python client
ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]


### Helper functions
voice=voices()
async def segment_paragraphs(text):
    # Split the text into paragraphs
    paragraphs = text.split("\n\n")
    return paragraphs
#def label_paragraphs(paragraphs):
    labeled_paragraphs = []
    for idx, paragraph in enumerate(paragraphs):
        labeled_paragraphs.append(f"Paragraph {idx + 1}: {paragraph}")
    return labeled_paragraphs

async def generate(paragraphs,ToAudio):
    for index,paragraph in enumerate(paragraphs):
        audio=ToAudio(paragraph)
        elevenlabs.save(audio,"output/clip_"+str(index)+".mp3")
async def ToAudio(element):
    if element.startswith("Tom:"):
        element=element[len("Tom:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[1])
        return audio
    elif element.startswith("Alice:"): 
        element=element[len("Alice:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[0])
        return audio
    elif element.startswith("[Intro"):
        element=element[len("[Intro"):].strip()
        with open('crime_intro.mp3', 'rb') as file:
            audio = file.read()
        return audio
    elif element.startswith("[Outro"):
        element=element[len("[Outro"):].strip()
        with open('crime_outro.mp3', 'rb') as file:
            audio = file.read()
        return audio   
     
async def glue(paragraphs):
    concatenated_audio = AudioSegment.silent(duration=0)
    for index,paragraph in enumerate(paragraphs):
        audio = AudioSegment.from_mp3("output/clip_"+str(index)+".mp3")
        concatenated_audio += audio
    return concatenated_audio

async def preprocess(text,filepath):
        paragraphs = segment_paragraphs(text)
        
        paragraphs=paragraphs[:-2]
        print(paragraphs)


        # Print the labeled paragraphs
        generate(paragraphs,ToAudio)
        #glue(audiofiles)
        finalaudio=glue(paragraphs)
        finalaudio.export(filepath,format="mp3")
        #elevenlabs.save(finalaudio, filepath)


async def submit_to_elevenlabs(text, file_path):
    """Adapted from TextToAudio/audiooutputtest.py

    Note: Presumably for scalability the API key will need to be passed in somehow.
    Also note that there appears to be an async option for the python client which
    should be usable in the current async context if desired. Since this fetch is
    done in a background task, it might not really matter that much.
    """
    preprocess(text, file_path)

    #elevenlabs.save(finalaudio, file_path)



""" 
   voice_id = "ZQe5CZNOzWyzPSCn5a3c"
    voice = elevenlabs.Voice(
        voice_id = voice_id,
        settings = elevenlabs.VoiceSettings(
            stability = 1,
            similarity_boost = 0.75
        )
    )
    audio=elevenlabs.generate(
        text=text,
        voice=voice
    )
    elevenlabs.save(audio, file_path)"""



# Background task for submitting text to ElevenLabs
async def generate_voice(text, user_id, job_id):
    file_path = f"files/{user_id}/{job_id}.mp3"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    await submit_to_elevenlabs(text, file_path)


### Endpoint handlers

async def create(request):
    data = await request.json()
    user_id = data["userId"]
    text = data["text"]
    print(text)
    job_id = str(uuid.uuid4())
    background_tasks = BackgroundTasks()
    background_tasks.add_task(generate_voice, text, user_id, job_id)
    return JSONResponse({"jobId": job_id}, background=background_tasks)


async def status(request):
    job_id = request.path_params["job_id"]
    # Implement logic to check job status
    # This is a placeholder response and does not indicate true status
    return JSONResponse({"status": "complete", "jobId": job_id})


async def speech(request):
    job_id = request.path_params["job_id"]
    user_id = request.query_params["userId"]
    file_path = f"files/{user_id}/{job_id}" # Replace with actual path to the audio file
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return JSONResponse({"error": "File not found"}, status_code=404)


async def files(request):
    user_id = request.query_params["userId"]
    directory = f"files/{user_id}/"
    if not os.path.exists(directory):
        return JSONResponse({"error": "User files not found"}, status_code=404)
    file_list = os.listdir(directory)
    return JSONResponse({"files": file_list})


### Application setup

routes = [
    Route("/create", create, methods=["POST"]),
    Route("/status/{job_id}", status, methods=["GET"]),
    Route("/speech/{job_id}", speech, methods=["GET"]),
    Route("/files", files, methods=["GET"])
]


app = Starlette(debug=True, routes=routes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],  # Or specify just ["GET", "POST"]
    allow_headers=["*"],  # Adjust according to what headers you need
)
