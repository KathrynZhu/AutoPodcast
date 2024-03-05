import asyncio
import elevenlabs
import os
import requests
import uuid
import shutil
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, FileResponse
from starlette.background import BackgroundTasks
from starlette.routing import Route
from elevenlabs import voices
from pydub import AudioSegment
from pydub.playback import play

elevenlabs.set_api_key("41b70d01d548863403dcc1c9c6434582")

# Not sure how this is used with the python client
ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]


### Helper functions
voice=voices()
def segment_paragraphs(text):
    # Split the text into paragraphs
    paragraphs = text.split("\n\n")
    print(paragraphs)
    return paragraphs
#def label_paragraphs(paragraphs):
    labeled_paragraphs = []
    for idx, paragraph in enumerate(paragraphs):
        labeled_paragraphs.append(f"Paragraph {idx + 1}: {paragraph}")
    return labeled_paragraphs

def generate(paragraphs,ToAudio):
    for index,paragraph in enumerate(paragraphs):
        # if paragraph.startswith("[Intro]"):
        #     intro_path = 'music/crime_intro.mp3'
        #     shutil.copy(intro_path, "output/clip_"+str(index)+".mp3")
        # elif paragraph.startswith("[Outro]"):
        #     outro_path = 'music/crime_outro.mp3'
        #     shutil.copy(outro_path, "output/clip_"+str(index)+".mp3")
        # else:
            # print("printing here in generate = " + paragraph)
            audio=ToAudio(paragraph)
            elevenlabs.save(audio,"output/clip_"+str(index)+".mp3")

# def ToAudio(element):
#     if element.startswith("Tom:"):
#         element=element[len("Tom:"):].strip()
#         audio=elevenlabs.generate(
#         text=element,
#         voice=voice[1])
#         return audio
#     elif element.startswith("Alice:"): 
#         element=element[len("Alice:"):].strip()
#         audio=elevenlabs.generate(
#         text=element,
#         voice=voice[13])
#         return audio
#     elif element.startswith("[Intro"):
#         element=element[len("[Intro"):].strip()
#         with open('music/crime_intro.mp3', 'rb') as file:
#             audio = file.read()
#         return audio
#     elif element.startswith("[Outro"):
#         element=element[len("music/[Outro"):].strip()
#         with open('music/crime_outro.mp3', 'rb') as file:
#             audio = file.read()
#         return audio   
     
def ToAudio(element):
    print("printing here in toaudio = " + element)
    if element.startswith("Alice:"):
        element=element[len("Alice:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[0])
        return audio
    elif element.startswith("David:"): 
        element=element[len("David:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[1])
        return audio
    elif element.startswith("Tom:"): 
        element=element[len("Tom:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[2])
        return audio
    elif element.startswith("Maddy:"): 
        element=element[len("Maddy:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[3])
        return audio   
    elif element.startswith("Josh:"): 
        element=element[len("Josh:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[3])
        return audio  
    elif element.startswith("Annabelle:"):
        element=element[len("Annabelle:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[13])
        return audio
    elif element.startswith("Ryan Gosling:"): 
        element=element[len("Ryan Gosling:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[14])
        return audio
    elif element.startswith("Drake:"): 
        element=element[len("Drake:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[15])
        return audio
    elif element.startswith("Lin Manuel Miranda:"): 
        element=element[len("Lin Manuel Miranda:"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[16])
        return audio   
    elif element.startswith("Donald Trump:"): 
        element=element[len("Donald Trump"):].strip()
        audio=elevenlabs.generate(
        text=element,
        voice=voice[17])
        return audio
    elif element.startswith("[Intro]"):
        element=element[len("[Intro]"):].strip()
        with open('music/crime_intro.mp3', 'rb') as file:
            audio = file.read()
        return audio
    elif element.startswith("[Outro]"):
        element=element[len("[Outro]"):].strip()
        with open('music/crime_outro.mp3', 'rb') as file:
            audio = file.read()
        return audio 

def glue(paragraphs):
    concatenated_audio = AudioSegment.silent(duration=0)
    for index,paragraph in enumerate(paragraphs):
        audio = AudioSegment.from_mp3("output/clip_"+str(index)+".mp3")
        concatenated_audio += audio
    return concatenated_audio

async def preprocess(text,filepath):
        paragraphs = segment_paragraphs(text)
        #paragraphs=paragraphs[:]
        print(paragraphs)


        # Print the labeled paragraphs
        generate(paragraphs,ToAudio)
        #glue(audiofiles)
        finalaudio= glue(paragraphs)
        finalaudio.export(filepath,format="mp3")
        #elevenlabs.save(finalaudio, filepath)

async def submit_to_elevenlabs(text, file_path):
    """Adapted from TextToAudio/audiooutputtest.py

    Note: Presumably for scalability the API key will need to be passed in somehow.
    Also note that there appears to be an async option for the python client which
    should be usable in the current async context if desired. Since this fetch is
    done in a background task, it might not really matter that much.
    """
    # voice_id = "ZQe5CZNOzWyzPSCn5a3c"
    # voice = elevenlabs.Voice(
    #     voice_id = voice_id,
    #     settings = elevenlabs.VoiceSettings(
    #         stability = 1,
    #         similarity_boost = 0.75
    #     )
    # )
    # audio=elevenlabs.generate(
    #     text=text,
    #     voice=voice
    # )
    # elevenlabs.save(audio, file_path)
    await preprocess(text, file_path)



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

